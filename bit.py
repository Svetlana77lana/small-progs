# -*- coding: utf-8 -*-
# битовые операции
двоичной (префикс 0b)
восьмеричной (префикс 0o) и шестнадцатеричной (префикс 0x) системах счисления.

# запись числа в определенные биты числа
x = 5
y = 10
# Умножить 2-4 биты первого числа на 0-5 биты второго числа
x &= 0b11100
y &= 0b11111
print "x = ", x,", y = ", y

temp = 0xFFFFFFFF
temp |= 0x1
print bin(temp)
temp &= 0xFFFFFF8F	# обнуление 4-6 разрядов
print bin(temp)
temp |= 0x20 # установка значения 010 в 4-6 разряды
print bin(temp)

PORTB = 3 #011
# установить нулевой бит
PORTB |= 0x01
print(bin(PORTB))
# сбростить нулевой бит
PORTB &= ~0b01
print(bin(PORTB))
#проверить установлен ли бит
print("yes") if (PORTB & 0x01) else ("no")
#	x = 3 if x>1 else 2
	
print(x << 3)
print(y >> 1) # при у=10, даст 5 - деление на 2^^1 разряд

a &= 0xFF00 # обнулим младшие 8 разрядов 0-7
a |= (ch&0x00FF) # обнулим старшие 8 бит 15-8 и а+ch

b = 0x110 #0b10001 0000
b &= 0x17F #10111 1111
b |= 0x80 # 01000 0000
print(bin(b) # 0b11001 0000


a = 0b100000
a |= 0x10
a &= 0XFFFFFFF0
print(bin(a))
a |= 4
print(bin(a))


t = (0x410)
print bin(t) 
t &= ~0x10
print t
print bin(t)

temp &= 0b1 # выбирается младший бит, остальные обнуляются

x = 15
y = 18
# x &= 0b11100
# y &= 0b11111
print "x = ", bin(x),", y = ", bin(y)

x = x << 2
print bin(x)
x = x >> 2
print bin(x)
print x

