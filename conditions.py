def print_numbers(n):
    numbers = range(n)
    for number in numbers:
        print(number)
        
 
def print_odd_numbers(n):
     numbers = range(n)
     for number in numbers:
         if number%2 != 0:
             print(number)       
 
 
 
def print_even_numbers(n):
     numbers = range(n)
     for number in numbers:
         if number%2==0:
             print(number)            
  
  
def odd_or_even(n):
    numbers = range(n)
    for number in numbers:
        if number%2==0:
            print(f"{number} is even ")
        else:
            print(f"{number} is not even")         
            
            
def check_divisibility(n):
    numbers = range(n)
    for number in numbers:
        if number%2==0:
            print(f"{number} is divisible by 2")
        elif number%3==0:
            print(f"{number} is divisible by 3")
        elif number%5==0:    
            print(f"{number} is divisible by 5")   
        else: 
            print(f"{number} is not divisible by 2,3 or 5")  
            
            
# create a function named fizzbuzz that accepts a number n and generates(foxx )
def check_number(n):
    numbers_int(n)
    for number in numbers:
        if number%3 !=0 :
            print("fizzbuzz")
        elif number % 3 ==0:
            print("fizz")   
        elif number % 5 ==0:
            print("buzz")    
        else:
            print(number)    



def countdown(n):
    while n >0:
        print(n)
        n-=1
 
    
def count_down_to_five(n):
    for number in numbers
    while n >0:
        print(n)
        if n ==5:
           break
        n-=1
        
def divisible_by_seven(n):
    x = 0
    while x<= n :
        x+=1
        if x%7 !=0:
            continue
        print(f"{x} is divisble by 7")   
        
        
#  using while, if and continue print all the add numbers between 0 and 100       
# def odd_numnbers(n):
#     x = 0 
    