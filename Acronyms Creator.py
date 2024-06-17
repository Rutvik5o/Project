#using function of splitting & indexing

input_string=input("Enter your phase=> \n")

text=input_string.split() #using splitting function


#using indexing via for loop

n=" "

for i in text:
    n= n+str(i[0]).upper()
print(n)




