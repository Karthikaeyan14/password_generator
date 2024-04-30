import random

letter=('a,b,c,d,e,f,g,h,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z')
number=('1,2,3,4,5,6,7,8,9,0')
symbol=('@,#,$,%,^,&,*,(,)')

how_letter=int(input("How many letter do you want:"))
how_number=int(input("How many number do you want:"))
how_symbol=int(input("How many symbol do you want:"))
password_list=[]

for i in range(1,how_letter+1):
    char=random.choice(letter)
    password_list +=char


for i in range(1,how_number+1):
    char=random.choice(number)
    password_list+=char

for i in range(1,how_symbol):
    char=random.choice(symbol)
    password_list+=char

print(password_list)

random.shuffle(password_list)
print(password_list)

password=""

for i in password_list:
    password+=i

print(password)