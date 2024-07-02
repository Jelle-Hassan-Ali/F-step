# Strings with variables

string1 = "Hello Sir Welcome"
print (string1)

name1 = 'python'

message = 'is awesome programming language'

print (name1, message)

Course = '''Hi my name is Jelle Ali 

I'm beginniner of this python course'''

print(Course)

string2 = 'python for beginniners'

print(string2[0:7])

string3 = 'python for beginniners'

print(string3[7:10])

string4 = 'python for beginniners'

print(string4[10:-7])

# 👀

Course1 = 'python for intermediate'
another = Course1[:]

print(another)

# formatted strings

F_name = 'Jelle'
L_name = 'Ali'
message = F_name +'[' + L_name + '] is a programmer'

print(message)

frist = 'Adan'
last = 'Osman'
msg = f'{frist} [{last}] is a programmer'

print(msg)

# string methods

Course = 'Python Is Awesome Programming Language'
print(Course.upper())
print(Course.lower())
print(Course)
print(Course.find('Is'))
print(Course.replace('Awesome', 'imperessives '))

Course4 = 'Python For beginners'
print(Course4.replace('beginners', 'Absolute Beginners'))

NameP = 'Jelle Hassan Ali '
print('Ali' in NameP)

NameP = 'Jelle Hassan Ali '
print('Halima' in NameP)