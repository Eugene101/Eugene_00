#print ('Enter your number')
#x = input()
#y = x[::-1]

x=(input("Введите целое число: "))
if (x.isdigit()) == True:
    print ('Введено число:', x)
else: print ('Sorry, dude, it is not a integer',x)
x = int (x)
y = 0
z = x
while x > 0:
    mod= x%10
    x = x//10
    y = y*10+mod
print ('Исходное число:', z,'Развернутое число:', y)
if z == y: print ('Да, это палиндром')
else: print ('Неа, не палиндром')


