#List

num = [18,13, 14, 50,88,62,100,12,40]
lar = num[0]
for i in num:
    if i > lar:
        lar = i
print(lar)



matris = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for row in matris:
    for num in row:
        print(num)




numbers = [ 6,9,7,4]
numbers.insert(3 ,22)
print(numbers)


list = [8,3,5,7,1,6,2]
list.sort()
print(list)

list = [8,3,5,7,22,6,2]
list2 = list.copy()
print(list2)


numbers =[3,5,6,4,9,8,4]
numbers.d


# Remove duplicates

numbers = [3,5,6,4,9,8,4,6,8,2,2,1]
unique_numbers = list(set(numbers))
print(unique_numbers)
    
   
#Tuples
Ar = (1,2,3)
print(Ar)