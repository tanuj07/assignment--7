#Question 1
d={}
for i in range(1,5):
    key=input("enter the key: ")
    value=input("enter the value: ")
    d[key]=value
print(d)

#Question 2
d1={}
d2={}
for i in range(1,4):
    d2={}
    name=input("enter name")
    for j in range(1,4):
        sub=input("enter subject")
        marks=int(input("enter marks"))
        d2[sub]=marks
    d1[name]=d2
print(d1)
stud=input("enter the student's name whose marks u want to see")
print(d1[stud])