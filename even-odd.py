def even_or_odd(num):
    if num % 2 == 0:
        return True
    else:
        return False

number = int(input("Enter a number: "))

result = even_or_odd(number)

if result == True:
    print(str(number) + " is an even number")
else: 
    print(str(number) + " is an odd number")