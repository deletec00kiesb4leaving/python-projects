import random
import os
import sys 

os.system('cls' if os.name == 'nt' else 'clear')
character_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!#$%&()*+,-./:;<=>?@[]^_`{|}~"
# cyrillic_alphabet = "АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя"
# new_string = character_string + cyrillic_alphabet
# Uncomment the 2 lines above and replace every var from character_string to new_string
password = ""
entropy = 0

print(""" 

  _____                                    _    _____                           _             
 |  __ \                                  | |  / ____|                         | |            
 | |__) |_ _ ___ _____      _____  _ __ __| | | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
 |  ___/ _` / __/ __\ \ /\ / / _ \| '__/ _` | | | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
 | |  | (_| \__ \__ \\ V  V / (_) | | | (_| | | |__| |  __/ | | |  __/ | | (_| | || (_) | |   
 |_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_|  \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
                                                                                              
                                                                                              

""")

try:
    num_char = int(sys.argv[1])
except ValueError:
    print("Use  : python ./password_generator.py")
    print("Or   : python ./password_generator.py 'x'")
    print("With : 'x' for the number of character on your password")
    sys.exit(1)
except IndexError:
    num_char = int(input("How many characters should your password be? "))


def gen_pass(key, length):
    return random.sample(key, length)


def sum_pass(char_list):
    sum_password = ""
    for char in char_list:
        sum_password += char
    return sum_password


if num_char > len(character_string):
    entropy = num_char / len(character_string)

while entropy > 1:
    password_gen = gen_pass(character_string, len(character_string))
    password += sum_pass(password_gen)
    entropy -= 1
else: 
    new_entropy = round(entropy * len(character_string))

if num_char < len(character_string):
    password_gen = gen_pass(character_string, num_char)
else:
    password_gen = gen_pass(character_string, new_entropy)

password += sum_pass(password_gen)


print("\n-----BEGIN PASSWORD-----\n")
print(password)
print("\n-----END PASSWORD-----\n")
