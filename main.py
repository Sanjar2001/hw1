#1
name = input('Enter your name: ')
surname = input('Enter your surname: ')

print(f'Добро пожаловать в Полиннос, {name} {surname}!')

#2
first_student = input().strip()
second_student = input().strip()

if first_student == second_student * 4:
    print("True")
else:
    print("False")


#3
apples = int(input('How many apples have you eaten today? '))
bananas = int(input('How many bananas have you eaten today? '))
tomatoes = int(input('How many tomatoes have you eaten today? '))
calories = apples * 520 + bananas * 890 + tomatoes * 240
print(f'Today you consumed {calories}')

#4
max_weight = 50
quantity = 0
kilograms = 0
while kilograms < 50:
    kgs = int(input('How many kilos would you like to buy? '))
    if kilograms + kgs >= max_weight:
        break
    kilograms += kgs
    quantity = quantity + 1

print(kilograms)
print(quantity)


