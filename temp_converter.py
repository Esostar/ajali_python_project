# my temperature converter
# converting celcius to kelvin
def celcius_kelvine(x):
    res = x + 273
    return(res)

# converting  kelvin to celcius
def kelvin_celcius(x):
    res = x - 273
    return(res)

# converting fahrenheit to celcius
def fahrenheit_celcius(x):
    res = (5/9 *(x - 32))
    return(res)

# converting from celcius to fahrenheit
def celcius_fahrenheit(x):
    res = 1.8 * (x + 32)
    return(res)

# converting kelvin to rankine
def kelvin_rankine(x):
    res = 1.8 * (x + 0.6)
    return(res)

# converting fahrenheit to rankine
def fahrenheit_rankine(x):
    res = x + 460
    return(res)

# converting rankine to kelvine
def rankine_kelvin(x):
    res = 5/9 * (x - 0.6)
    return(res)

print("make a choice of temperature conversions from the list")
print("enter 1 to convert from celcius to kelvin")
print("enter 2 to convert from kelvin to celcius")
print("enter 3 to convert from fahrenheit to celcius")
print("enter 4 to convert from celcius to fahrenheit")
print("enter 5 to convert from kelvin to rankine")
print("enter 6 to convert from fahrenheit to rankine")
print("enter 7 to convert from rankine to kelvin")

while True:
    # asking user to make conversion choice input
    choice = input("enter choice number(1/2/3/4/5/6/7):  ")
    if choice in ('1', '2', '3', '4', '5', '6', '7'):
        x = float(input("enter first number:  "))
        

        if choice == '1':
            print(x, "celcius is equal to", celcius_kelvine(x),'k')

        elif choice == '2':
           print(x, "kelvin is is equal to", kelvin_celcius(x),'c')
        
        elif choice == '3':
            print(x, "fahrenheit is equal to", fahrenheit_celcius(x),'c')
        
        elif choice == '4':
            print(x, "celcius is equal to", celcius_fahrenheit(x),'f')

        elif choice == '5':
            print(x, "kelvin is equal to", kelvin_rankine(x),'R')

        elif choice == '6':
            print(x, "fahrenheit is equal to", fahrenheit_rankine(x),'R')

        elif choice == '7':
            print(x, "rankin is equal to", rankine_kelvin(x),'k')


        nxt_cal = input("want to do another conversion? (yes or no):  ")
        if nxt_cal == "no":
            break

    else:
        print("invalid input")



