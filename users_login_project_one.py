from pystyle import *

print(Center.XCenter(Box.Lines("[+] Login Terminal [+]")))

user_message = """
[+] this program for login page
[+] write username and password
"""

Write.Print(user_message, Colors.red_to_purple)

print(Box.DoubleCube('Example [1]'))

while True:
    username = Write.Input('Write Username: ', Colors.blue_to_cyan)
    password = Write.Input('Write Password: ', Colors.blue_to_cyan)
    
    if username == 'admin' and password == '123':
        Write.Print('[+] Welcome Admin\n', Colors.green)

        input('press any key to exit... ')
        exit()
    
    Write.Print("[+] Error Try Again\n", Colors.red)