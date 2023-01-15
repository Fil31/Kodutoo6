from math import *
from tkinter import ROUND
from datetime import date

def arithmetic(a1:float,sym:str,a2:float):
    """Lihtne kalkulaator
    + liitmine, - lahutamine, * korrutamine, /jagamine
    a1 1st numb
    a2 2nd numb
    str sym tehe
    rtype 
    """
    if sym in ["+","-","/","*"]:
        if sym=="/" and a2==0:
            vastus="Div/0"
        else:
            vastus=eval(str(a1)+sym+str(a2))
    else:
        vastus="Tundmatu tehe!"
    return vastus

#Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения: периметр квадрата, площадь квадрата и диагональ квадрата.
def square(b1:int):
    b1=int(b1)
    if b1!=0:
        perimetr=b1*4
        ploshad=b1*b1 
        diagonal1=(2*b1**2)
        diagonal2=sqrt(diagonal1)
    else:
        ans="Error"
        return ans
    return diagonal2, ploshad, perimetr
#Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный, и False иначе.
def is_year_leap(b2:int):
    if b2%4==0:
        year="Высокосный"
    else:
        year="Невысокосный"
    return year
#Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года, которому этот месяц принадлежит (talv, kevad, suvi или sügis).
def season(b4:int):
    if b4>=1 and b4<3:
        month="talv"
    elif b4>=3 and b4<5:
        month="kevad"
    elif b4>=6 and b4<9:
        month="suvi"
    elif b4>=9 and b4<=11:
        month="sugis"
    elif b4==12:
        month="talv"
    else:
        error1="Error"
        return error1
    return month
#Пользователь делает вклад в размере a евро сроком на years лет под 10% годовых (каждый год размер его вклада увеличивается на 10%. Эти деньги прибавляются к сумме вклада, и на них в следующем году тоже будут проценты).
#Написать функцию bank, принимающая аргументы a и years, и возвращающую сумму, которая будет на счету пользователя.
def years1 (a:int,years:int):
    while years !=0:
        a+=a*1.1-a
        years -= 1
    return a
#Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, и возвращающую True, если оно простое, и False - иначе.
def is_prime(int4:int):
    int4=int(int4)
    if int4>0:
         k = 0
         for i in range(2, int4 // 2+1):
            if (int4 % i == 0):
                k = k+1
         if (k == 0):
            otvetik="Число простое"
         else:
            otvetik="Число не является простым"
    else:
        otvetik="Error"
        return otvetik
    return otvetik
#Написать функцию date, принимающую 3 аргумента — день, месяц и год. Вернуть True, если такая дата есть в нашем календаре, и False иначе.

def is_valid_date(day, month, year):
    try:
        date(year, month, day)
        print(True)
        return True
    except ValueError:
        print(False)
        return False

#Написать функцию XOR_cipher, принимающая 2 аргумента: строку, которую нужно зашифровать, и ключ шифрования, которая возвращает строку, зашифрованную путем применения функции XOR (^) над символами строки с ключом. 
def XOR_cipher(password,key):
    c = password ^ key
    print(f"Зашифрованный пароль: {c}")
    return c
#Написать также функцию XOR_uncipher, которая по зашифрованной строке и ключу восстанавливает исходную строку.
def XOR_uncipher(dekey,key):
    c = dekey ^ key
    print(f"Расшифрованный пароль: {c}")
    return c
