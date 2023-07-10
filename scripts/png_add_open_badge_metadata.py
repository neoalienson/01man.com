import json
import hashlib
from PIL import Image, PngImagePlugin

# Read the image from the local file
pathname = "alibaba_cloud_certified_alibaba_big_data_associate.png"
img = Image.open(pathname)

# Prepare the metadata
metadata = {
    "@context": "https://w3id.org/openbadges/v2",
    "type": "Assertion",
    "issuedOn": "2023-06-14T12:02:10.852381+00:00",
    "image": f"https://01man.com/about-me/{pathname}"
}


# Embed the metadata into the image as a comment
img_text = json.dumps(metadata, ensure_ascii=False)
png_info = PngImagePlugin.PngInfo()
png_info.add_itxt("openbadges", img_text)
img.save(pathname, "PNG", pnginfo=png_info)

print(f"Badge image saved as '{pathname}'.")