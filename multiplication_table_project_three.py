from pystyle import *

print(Center.XCenter(Box.Lines("Multiplication Table")))

Write.Print("[-] this progranm for simple cal\n", Colors.red_to_purple, interval=0.01)


while True:
    number = int(Write.Input('[+] Write your Number here: ', Colors.blue_to_purple, interval=0.01))

    for i in range(1, 11):
        Write.Print(f'{number} x {i} = {(number * i)}\n', Colors.white, interval=0.01)

    instructions = '''
[Continue] -> Press ('y' | 'Y')
[Exit] -> Press any key
'''
    choice = Write.Input(Box.SimpleCube(instructions), Colors.green_to_cyan, interval=0.01)

    if choice.lower() == 'y':
        continue
    else:
        break
