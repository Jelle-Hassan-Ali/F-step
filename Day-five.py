
    
# Logical Operators

has_hight_income = True
has_good_credit = True

if has_hight_income and has_good_credit:
    print("Eligible for loan")
    
has_hight_income = False
has_good_credit = True

if has_hight_income and has_good_credit:
    print("Eligible for loan")
    
else:
    print(" not available")  
    
has_hight_income = False
has_good_credit = True

if has_hight_income or has_good_credit:
    print("Eligible for loan")   
    

has_hight_income = True
has_good_credit = False

if has_hight_income and not has_good_credit:
    print("Eligible for loan")       
    
has_hight_income = False
criminal_record = True

if has_hight_income and criminal_record:
    print("Eligible for loan")
    
    
tempreture = 30

if tempreture >= 30:
    print(" it is a hot day please drink more water")
    
elif tempreture <= 10:
    print("It is a cold day please wear warm clothes")



Name = "Jelle"

if len(Name) <3:
    print("Name must be at least 3 characters long")
    
elif len(Name) >5:
    print("Name must be at most at least 5 characters long") 
    
else:
    print("Name is looks good")       
