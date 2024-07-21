#  Basic function

def greating():
    print("Hello")
    print("Jelle")
    
greating()

# Arguments functions

def my_function(Fname , Lname , Age):
    print("Hello", Fname, Lname , Age)
    
my_function("Jelle", "Hassan" , "Yor age is : 23 ")

def my_function(fname, lname ,tname):
  print("My Name is ",fname + lname + tname)

my_function("Jelle ", " Hassan" , " Ali")

# Arbitrary *args functions

def my_fun(*kids):
    print("The youngest child is: ", kids[3])
    
my_fun("Jelle", "Liban", "Mahamed", "Abdi Majid", "Ahmed", "Iqro")    

# Keyword Arguments

def my_func(child1, child2, child3, child4, child5,):
    print("The youngest child is", child3)
    
my_func(child1= "Abdi Majid", child2= "Ahmed", child3= "Adan", child4= "fatma", child5= "Ali")    

def my_func(child1, child2, child3, child4):
    print("The oldest child is", child2)
    
my_func("Jelle", "Kulane", "Barre", "Ali")    


# Arbitrary Keyword Arguments, **kwargs

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Jelle", lname = "Ali")


# Default Parameter Value

def my_function(region = "Hiran"):
  print("I am from " + region)
my_function("Mudug")
my_function("Bari")
my_function()
my_function("Nugal")

def my_function(region = "Bari"):
  print("I am from " + region)

my_function()

# passing list as an argument

def my_function(food):
    for x in food:
        print(x)
fruit = ["Qare", "Liin","Mos","Cambe","Qajar","Babay"]  
    
my_function(fruit)      

# Return Values

def my_function(x):
    return x*2

print(my_function(5))
print(my_function(6))
print(my_function(7))


# Positional-Only Arguments

def my_function(x, /):
  print(x)

my_function(3)

