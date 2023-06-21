import json
import hashlib
from PIL import Image, PngImagePlugin

# Read the image from the local file
img = Image.open(image_file)

# Prepare the metadata
metadata = {
    "@context": "https://w3id.org/openbadges/v2",
    "type": "Assertion",
    "issuedOn": "2023-06-14T12:02:10.852381+00:00",
    "image": "https://01man.com/about-me/alibaba_cloud_native_associate.png"
}


# Embed the metadata into the image as a comment
img_text = json.dumps(metadata, ensure_ascii=False)
png_info = PngImagePlugin.PngInfo()
png_info.add_itxt("openbadges", img_text)
img.save("badge_with_metadata.png", "PNG", pnginfo=png_info)

print("Badge image saved as 'badge_with_metadata.png'.")