# Unpacking

cordinates = (4,5,6)
cordinates[0]*cordinates[1]*cordinates[2]
print(cordinates[0])


cordinates = (2,4,7)

x = cordinates[0]
y = cordinates[1]
z = cordinates[2]
print(x*y*z)



# Dictionary

Customer = {
    "name": "Jelle Ali",
    "Age": 24,
    "is_active":False,
    "city": "Dhaxtaal",
    "birthday":2024,
    

}

Customer["name"] = "Hassan"
Customer["mother"]= "Amina"

print(Customer["mother"])


phone = input("phone: ")

digits_mapping ={
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "0": "zero"
    
}

output = ""
for ch in phone:
    output += digits_mapping.get(ch,"!") + " "
print(output)
    