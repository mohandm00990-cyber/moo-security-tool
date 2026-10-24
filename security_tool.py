import random
import string

def banner():
    print("\n  __  __                ____")
    print(" |  \\/  | ___   ___    / ___|")
    print(" | |  | | (_) | (_) |   ___) |")
    print(" |_|  |_|\\___/ \\___/   |____/")
    print("  >> By Moo - The Ethical Hacker <<")
    print("  >> Protect, Don't Hack <<\n")

def check_password(p):
    score = 0
    if len(p) >= 8:
        score += 1
    if any(c.isdigit() for c in p):
        score += 1
    if any(c.isupper() for c in p):
        score += 1
    if any(c in "@#$%&_!" for c in p):
        score += 1
    print("--- النتيجة ---")
    if score == 4:
        print("ممتاز باسورد قوي جدا ممتاز")
    elif score == 3:
        print("كويس بس ممكن اقوى")
    else:
        print("ضعيف جدا")

def gen():
    l = int(input("عايز كام حرف؟ "))
    chars = string.ascii_letters + string.digits + "@#$%&*!"
    pw = random.choice(string.ascii_uppercase)
    pw += random.choice(string.digits)
    pw += random.choice("@#$%&*!")
    pw += "".join(random.choice(chars) for _ in range(l-3))
    pw = "".join(random.sample(pw, len(pw)))
    print("\nباسوردك: " + pw)
    check_password(pw)

banner()
while True:
    print("\n===== Moo Security Tool =====")
    print("1- افحص باسورد")
    print("2- ولد باسورد قوي")
    print("3- خروج")
    c = input("اختر رقم: ")
    if c == "1":
        p = input("اكتب الباسورد: ")
        check_password(p)
    elif c == "2":
        gen()
    elif c == "3":
        print("باي باي يا بطل Moo!")
        break
