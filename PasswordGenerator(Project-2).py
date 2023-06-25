import random
letters=['A','B','C','D','E','F','G','H','I','G','K','L','M','N','O','P','Q','R','S','T','U'
      ,'V','W','X','Y', 'Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
      'q','r','s','t','u','v','w','x','y','z']

symbols=['!','@','#','$','%','^','&','*','(',')','-','_','+','_','=']

numbers=['1','2','3','4','5','6','7','8','9']

print("Welcome to Password Generator")

n_letter=int(input("How many letters you want in your Password\n"))

n_symbol=int(input("How many symbol you want in your Password\n"))

n_number=int(input("How many number you want in your Password\n"))

password_list=[]

for i in range(1,n_letter+1):
    char=random.choice(letters)
    password_list += char

for i in range(1,n_letter+1):
    char=random.choice(symbols)
    password_list += char


for i in range(1,n_letter+1):
    char=random.choice(numbers)
    password_list += char

print(password_list)


random.shuffle(password_list)

print(password_list)

password=""

for char in password_list:
    password += char

print(password)








