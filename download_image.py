from pystyle import *
import urllib.request as uq
Write.Print("[+] this program for download images\n", Colors.red, 0.01)

Write.Print(Box.DoubleCube("Example 11"), Colors.white, 0.01)

image_url = Write.Input("Enter image URL here: ", Colors.blue_to_cyan, 0.01)
image_name = Write.Input("Enter image Name here: ", Colors.blue_to_cyan, 0.01)
try:
    uq.urlretrieve(image_url, f"{image_name}.jpg")

    Write.Print(f"\n[+] Image downloaded successfully: {image_name}", Colors.green, 0.01)
except Exception as ex:
    Write.Print(f"\n[-] Error: {ex}", Colors.red, 0.01)