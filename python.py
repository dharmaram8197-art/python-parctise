'''import keyword
print(keyword.kwlist)

a=None
print(a)


a=10 
print(bool(a)) 

a=15.2
print(bool(a))





a=10
print(float(a))   
a=5+0j
print(a)
a=6j
print(a)
a="happy father's day" 
print(len(a))'''



'''
a={'a':10}
print(a)
a={'a':[10,20,30],'b':40}
print(a['a'][-2]) 
print(a)'''


'''a="hello"
print(a[2:4+1:1])
print(a[-3:-2+1])'''

'''a="Good morning"
print(a[7:10+1:1])
print(a[-5:-1])'''
'''
a="hello" 
print(a[4:0-1:-1])
print(a[::-1])'''

'''a='Good Morning'
print(a[5:13+1:3])
print(a[-7::3])
print(len(a[-4:-6:-1]))
print(len(a[10:4-1:-3])) '''

'''a=int(input("enter the number"))
print(a,type(a))'''

'''a=eval(input("enter:"))
print(a,type(a))'''

'''a=int(input("enter :"))
if a%2==0:
    print("even")
else:
    print("odd")'''

"""a=eval(input("enter a list "))
if len(a)==5:
 print("length of list is 5")
else:
 print("no")"""


'''
print(ord("b"))
print(ord("B"))
print(chr(97))'''


'''ch=input("enter:")
if "A"<=ch<="Z":
    print("uppercase")
elif "a"<=ch<="z":
    print("lowercase")
else:
    print("not an alphabet")'''

"""un=input("enter:")
if un=="admin":
    pwd=input("enter password:")
    if pwd=="admin123":
        print("login sucessfull")
    else:
        print("invalid password")"""

'''
usename="hero"
password="hero123"

un=input("enter the username:")
if un==usename:
    pw=input("enter the password:")
    if pw==password:
        print("login successfull")
    else:
        print("invalid password")
else:
    print("invalid username")
'''
'''
i=1
while i<=50:
    if i%2==0:
        print(i)
    i+=1
'''
'''i=2
while i<=50:
    print(i)
    i+=2'''



'''n=int(input("enter the number:"))
rev=0
while n>0:
    id=n%10
    n=n//10
    rev=rev*10+id
    print(rev)
''' 

'''for i in range(0,101):
    print(i)'''

'''s=input("enter:")
for i in s:
    if "A"<=i<="Z":
        out+=chr(ord(i)+32)
    elif "a"<=i<="z":
        out+=chr(ord(i)-32)
    else:
        out+=i
print(out)        '''

'''s=input("enter:")
rev=""
for i in s:
    rev=i+rev
print(rev)''' 

'''
for i in range(1,6):
   for j in range(1,6):
     if i==j:
       print("1",end="")
     else:
        print("@",end=" ")
print()'''
