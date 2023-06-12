import json
import getpass
import random
from colorama import init, Fore
init(autoreset=True)
import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 120)  # 120 words per minute
engine.setProperty('volume', 2)  # 200% volume
User = getpass.getuser()
cash = []
Session = True
with open("Data.json", "r") as x:
    Data = json.load(x)
    RAM = Data
def add_item(): # Функция пополнения базы данных
    Key = request
    print(Fore.RED + "Unvalid request, please input variant of answer:")
    engine.say("Unvalid request, please input variant of answer:")
    engine.runAndWait()
    Value = str(input())
    cash.append(Key)
    cash.append([Value])
print(Fore.GREEN + "Hello, " + User + "!", sep="")
engine.say("Hello, " + User + "!")
engine.runAndWait()
print(Fore.GREEN + "Data size = " + str(len(Data)))
engine.say("Data size = " + str(len(Data)))
engine.runAndWait()
while Session:
    if len(cash) > 0:
        RAM[cash[0]] = cash[1]
        with open("Data.json", "w") as x:
            json.dump(RAM, x, sort_keys=True, indent=2)
        cash.clear()
        print("cash have new element")
        engine.say("cash have new element")
        engine.runAndWait()
    request = input()
    if Data.__contains__(request):
        num = len(Data[request]) - 1
        print(Fore.GREEN + Data[request][random.randint(0, num)])
        engine.say(Data[request][random.randint(0, num)])
        engine.runAndWait()
    else:
        add_item()









