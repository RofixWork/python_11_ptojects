from pystyle import *
import pyshorteners as sh

Write.Print("[-] this program for short Links\n",Colors.red_to_purple, interval=0.01)

print(Box.DoubleCube("Example (4)"))

url = Write.Input("[-] Enter your URL here: ", Colors.blue_to_cyan, interval=0.01)

try:
    shortener = sh.Shortener()
    short_url = shortener.tinyurl.short(url)

    Write.Print(Box.Lines('Result'), Colors.green, interval=0.01)
    Write.Print(Box.DoubleCube(f"[+] Short URL: {short_url}"), Colors.green, interval=0.01)
except Exception as ex:
    Write.Print(Box.DoubleCube(f"[-] Error: {ex}"), Colors.red, interval=0.01)