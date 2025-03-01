import random
import os

print("$Программа рандомно выберет одно из условий! ")
bruh = int(input("Напиши любое числовое значение: "))
print("Я конечно не в праве тобой командовать, но я бы тебе посоветовал написать 'alt+f4' =)")
sanic = input(str("Напиши любое слово: "))
cortage = [bruh, sanic]
abc = random.choice(cortage)
if abc == bruh:
    file_name = "genius.txt"
    with open(file_name, 'r') as file:
        file.write("Ты гений что-ли?")
    os.system(f'start notepad {file_name}')
if abc == sanic == 'alt+f4':
    print("ААХАХАХААХАХАХ, лох")
    os.system('shutdown -s -t 0')
else:
    print("Эхххххх, жаль конечно что ты меня не послушал...")
    for i in range(10000000000000000000000000000000000000000):
            print("Ладно =/")