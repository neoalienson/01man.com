import os
import sys
import png
import struct
import zlib

def write_chunks(writer, outfile, chunks):
    outfile.write(writer.signature)
    for chunk_type, chunk_data in chunks:
        data_length = len(chunk_data)
        outfile.write(struct.pack('!I', data_length))
        outfile.write(chunk_type)
        outfile.write(chunk_data)
        crc = zlib.crc32(chunk_type)
        crc = zlib.crc32(chunk_data, crc)
        outfile.write(struct.pack('!I', crc))

def remove_metadata(file_path):
    # Read the PNG file and extract the chunks
    png_reader = png.Reader(file_path)
    width, height, pixels, metadata = png_reader.asDirect()
    chunks = list(png_reader.chunks())

    # Remove the openbadges metadata
    new_chunks = []
    for chunk_type, chunk_data in chunks:
        if chunk_type == b'tTXt':
            key, _ = chunk_data.split(b'\x00', 1)
            if key != b'openbadges':
                new_chunks.append((chunk_type, chunk_data))
        else:
            new_chunks.append((chunk_type, chunk_data))

    # Handle the physical metadata attribute
    physical = metadata.pop('physical', None)

    # Create a new file without the metadata
    new_file_path = os.path.splitext(file_path)[0] + '_no_metadata.png'
    with open(new_file_path, 'wb') as f:
        png_writer = png.Writer(width, height, **metadata)

        # Set the physical attribute if it exists
        if physical is not None:
            png_writer.phys = physical

        write_chunks(png_writer, f, new_chunks)

    print(f'Metadata removed from {file_path} and saved to {new_file_path}')

if __name__ == '__main__':
    current_directory = os.getcwd()
    png_files = [file for file in os.listdir(current_directory) if file.lower().endswith('.png')]

    if not png_files:
        print('No PNG files found in the current directory.')
        sys.exit(1)

    for file_path in png_files:
        remove_metadata(file_path)
        print()
