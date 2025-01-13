def greet(name):
    return "Привет, "+name+"!"
def square(number):
    return number**2
def max_of_two(x,y):
    if x>y:
        return x
    else:
        return y


def describe_person(name,age=30):
    return "Имя: "+name, "Возраст: "+str(age)

def is_prime(number):
    for i in range(2,int(number**0.5)+1):
        if number%i==0:
            return False
    return True