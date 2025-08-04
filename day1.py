def add(a,b):
    a+b

def subtract(a,b):
    a-b

def multipy(a,b):
    a*b

def divide(a,b):
    a/b

print("Select an Operator")
print("1 = +")
print('2 = -')
print('3 = *')
print('4 = /')  

while True:
    i=input("chose operator(1/2/3/4):")

    if i in ('1','2','3','4'):
        try:
            num1=float(int(input("Enter 1st no.")))
            num2=float(int(input('enter 2nd no.')))
        except ValueError:
            print('invalid input')
            continue
        
        if i == '1':
            print(num1 + num2)
        elif i == '2':
            print(num1 - num2)
        elif i == '3':
            print(num1 * num2)
        elif i == '4':
            if num1==0:
                raise ZeroDivisionError("cannot divide by zero")
            elif num2==0:
                raise ZeroDivisionError('not divisible by zero')
            else:
                print(num1 / num2)

        next=input('want to try again?(yes/no)')
        if next == 'no':
         break

    else:
        print("invalid output")