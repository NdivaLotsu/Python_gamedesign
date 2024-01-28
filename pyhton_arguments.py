# Python args and kwargs

# Collecting information from users example an addition calculator.

# first approach
#num1 = int(input("Enter first number: "))
#num2 = int(input("Enter second number: "))
#num3 = int(input("Enter third number: "))

def add(first_number,second_number,third_number):
    return first_number + second_number + third_number

# print(add(num1,num2,num3))

my_list = [1,2,3,4,5,6,7]

def get_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

# print(get_sum(my_list))

# Accept multiple parameters in python using *args
# * means to accept unlimited number of arg
def calculate(*numbers):
    print(numbers)

# calculate(1,2,3,4,5,6,7,8,9,10)
    
def calculate_sum(*numbers):
    print(numbers)
    total = 0
    for number in numbers:
        total += number

    return total

# print(calculate_sum(1,2,3,4,5,20,60,100,120))

def collect_name(*names):
    for name in names:
        print("Hello ",name)

# collect_name("Ndiva","Kwame","Gwen","Vincent")

# Keyword args (**kwargs) to accept multiple key value pairs
def get_user(**user):
    print(user)

get_user(name="Ndiva",age= 11,location="Accra",favorite_food="Jollof")