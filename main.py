print("Добро пожаловать в калькулятор!")
number = input("Введите число: ")
is_digit = number.isdigit()
operation = input("Введите операцию: ")
number_2 = input("Введите второе число: ")
is_digit2 = number_2.isdigit()
if is_digit and is_digit2:
    if operation == "-":
        print("=", float(number)-float(number_2))
    elif operation == "+":
        print("=", float(number)+float(number_2))
    elif operation == "*":
        print("=", float(number)*float(number_2))
    elif operation == "/" or "|":
        print ("=", float(number)/float(number_2))
else:
        print("Пожалуйста, введите числа цифрами.")


