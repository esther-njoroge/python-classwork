def add(a, b):
    answer = a+b
    return answer 

def subtract(a,b):
    answer = a-b
    return answer

def multiply(c, d):
    answer = c*d
    return answer

def divide(a,b):
    answer = a/b
    return answer

def remainder(c, d):
    answer = c%d
    return answer

def power_of(e):
    answer = e*e
    return answer


# 
def sum(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total    

def multiplication(*nums):
    total = 1
    for num in nums:
        total *= num
    return total    

def create_sentence(**words):
    print (words)
    sentence = " "
    for word in words.values():
        sentence += word
        sentence += " "
    return sentence

def sum_and_greet(*args, **kwargs):
    total = 0
    for number in args:
      total += number
    # greeting = f"Hello {kwargs["first_name"]} {kwargs["last_name"]}, the sum of {list(args)} is {total}"  
    # return greeting     

    first name = kwargs['first_name'] 
   last_name = kwargs['last_name']
greeting = f"Hello {first_name} {last_name_}",the sum is {total}
return greeting

# # when calling
# sum_and_greet(10,20,30, first_name = "Nancy", last_name = "wainana")   
#                                                                 ...school = "akirachix", country="uganda"