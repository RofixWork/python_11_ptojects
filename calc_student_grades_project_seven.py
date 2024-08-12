from pystyle import *
import numpy as np
Write.Print("[+] this program for good student\n", Colors.orange, interval=0.01)

std_name = Write.Input("[-] Enter your name Here: ", Colors.purple, interval=0.01)

Write.Print(f"[+] Welcome {std_name.title()}\n", Colors.green, interval=0.01)

Write.Print(f"[-] Write your grades now\n", Colors.purple, interval=0.01)

grades = np.empty(4)
langs = np.array(['math', 'arabic', 'english', 'sport'])

#enter grades
for i in np.arange(4):
    grade = float(Write.Input(f"[+] Enter {langs[i]} grade: ", Colors.green_to_cyan, interval=0.01))

    assert grade >= 0 and grade <= 100, f"your grade out of range"

    grades[i] = grade

#print graddes
for grade, lang in np.stack((grades, langs), axis=1):
    Write.Print(f"[+]\t {lang} -> {str(grade).title()}\n", Colors.orange, interval=0.01)

sum_grades = np.sum(grades)
average_grades = grades.mean()
Write.Print(f"[+] Your full grade is {sum_grades}\n", Colors.green, interval=0.01)
Write.Print(f"[+] Your Average grade is {average_grades}\n", Colors.green, interval=0.01)

if average_grades > 60:
    Write.Print(Box.DoubleCube(f"[+] Congratulations, {std_name.title()}, you passed!\n"), Colors.green, interval=0.01)
else:
    Write.Print(Box.DoubleCube(f"[+] Sorry {std_name.title()}, you failed.\n"), Colors.red, interval=0.01)