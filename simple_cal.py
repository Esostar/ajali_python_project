def Add(x , y):
    plus = (x + y)
    return (plus)

def subtract(x , y):
    minus = (x - y)
    return (minus)

def multiply(x , y):
    times = (x * y)
    return(times)

def divide(x , y):
    divided = (x / y)
    return (divided)

print("make a choice of maths operation")
print("enter 1 for addition")
print("enter 2 for subtration")
print("enter 3 for multiplication")
print("enter 4 for division")

while True:
    choice = input("enter choice number(1/2/3/4):  ")
    if choice in ('1', '2','3','4'):
        num1 = int(input("enter first number:  "))
        num2 = int(input("enter second number:   "))

        if choice == '1':
            print(num1, '+', num2, '=', Add(num1, num2))

        elif choice == '2':
            print(num1, '-', num2, '=', subtract(num1, num2))
        
        elif choice == '3':
            print(num1, '*', num2, '=', multiply(num1, num2))
        
        elif choice == '4':
            print(num1, '/', num2, '=', divide(num1, num2))

        nxt_cal = input("want anither calculation? (yes or no):  ")
        if nxt_cal == "no":
            break

    else:
        print("invalid input")



