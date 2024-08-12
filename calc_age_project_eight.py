from pystyle import *
from datetime import datetime
Write.Print("[-] this program for age count\n", Colors.purple_to_red, 0.01)

Write.Print(Box.DoubleCube("Example 10"), Colors.white, 0.01)

def calc_age(date_of_birth : int) -> int:
    assert date_of_birth > 0, f"age must be grather than zero..."

    current_year = datetime.now().year

    return int(current_year) - date_of_birth

try:
    date_of_birth = int(Write.Input("[-] Write your birthday: ", Colors.blue_to_cyan, 0.01))

    Write.Print(Box.DoubleCube(f"[+] your age is {calc_age(date_of_birth)} years"), Colors.green, 0.01)
except Exception as ex:
    Write.Print(f"[!] Error: {ex}", Colors.red, 0.01)