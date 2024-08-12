from pystyle import *

Write.Print("[-] this program for calculator\n",Colors.red_to_purple, interval=0.01)

print(Box.DoubleCube("Example (2)"))

while True:
    number_one = Write.Input("[+] Write first Number: ",Colors.blue_to_green, interval=0.01)
    math_sign = Write.Input("[+] Write Math Code: ",Colors.orange, interval=0.01)
    number_two = Write.Input("[+] Write second Number: ",Colors.blue_to_green, interval=0.01)

    if math_sign not in ('+', '-', '/', '*'):
        Write.Print("[-] Invalid Math Code! Use (+, -, *, /)\n",Colors.red, interval=0.01)

    if not isinstance(float(number_one), float):
        Write.Print(f"[-] '{number_one}' not a number, Please Enter Numbers Only...\n",Colors.red, interval=0.01)

    if not isinstance(float(number_two), float):
        Write.Print(f"[-] '{number_two}' not a number, Please Enter Numbers Only...\n",Colors.red, interval=0.01)
        continue

    try:
        result = eval(f"{float(number_one)} {math_sign} {float(number_two)}")
        Write.Print(f"[+] Result: {result}", Colors.green, interval=0.01)
        exit()
    except ZeroDivisionError:
        Write.Print("[-] Error: Division by Zero!\n", Colors.red, interval=0.01)
    except Exception as e:
        continue