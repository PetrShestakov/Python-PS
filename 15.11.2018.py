# coding : utf-8


print("Привет !")
print("ДЗ Урок 1 normal")
name = input("Ваше имя:")

print(name,",добро пожаловать!")

answer = ''

while answer!= 'q':
 answer = input("давайте поработаем? (y/N/q)")
 if answer == 'y' and answer == 'y':
     print("отлично!")
     print('[1]- задача 1')
     print('[2] - задача 2')
     print('[3] - задача 3')
     do = int(input('Укажите номер действия:'))
     if do == 1:
          number = input('Введите число ')
          print(max(number))
     elif do == 2:
          first_number = input('Введите значение')
          second_number = input('Введите что-нибудь ещё ')
          second_number, first_number = first_number, second_number
          print(second_number, "Это было first_number")
          print(first_number, "Это было second_number")
     elif do == 3:
          print('ax**2+b*x+c=0')
          a = int(input('Введите a '))
          b = int(input('Введите b '))
          c = int(input('Введите c '))
          D = (b ** 2) - (4 * a * c)
          if D > 0:
              x1 = ((- b) - (D ** 0.5)) / (2 * a)
          x2 = ((- b) + (D ** 0.5)) / (2 * a)
          print('X1 =', x1)
          print('X2 =', x2)
     elif D == 0:
          x1 = (- b) / (2 * a)
          print('Уравнение имеет один корень X = ', x1)
     elif D < 0:
          print('Уравнение не имеет корней')
