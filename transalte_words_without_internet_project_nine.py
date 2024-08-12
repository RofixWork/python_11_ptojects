import json
from pystyle import *

Write.Print("[-] this program for translate\n",Colors.purple_to_red, interval=0.01)

print(Box.DoubleCube("Example (9)"))


while True:
    word = Write.Input("Write word your transalte here: ", Colors.blue_to_cyan, 0.01)

    with open("./english.json", 'r', encoding='utf-8') as file:
        words = json.load(file)
        is_word_exist = False

        for item in words:
            if word.lower().strip() == item['english'].lower():
                Write.Print(f"Translation: {item['arabic']}\n", Colors.green_to_yellow, interval=0.01)
                is_word_exist = True
                break
        
        if not is_word_exist:
            Write.Print(f"Translation {word} not found!\n", Colors.red_to_white, interval=0.01)