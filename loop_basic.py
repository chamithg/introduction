
from cgi import print_arguments
from math import e


print("basic")
for i in range (0,151):  
    print (i)

print("Multiples of Five ")
for i in range (0,1001):
    if(i%5 ==0):
        print(i)

print("Counting, the Dojo Way ")

for i in range(1,101):
    if(i%10 == 0):
        print("Coding Dojo")
    elif(i%5 == 0):
        print("Coding")
    else:
        print(i)
        
print("Whoa. That Sucker's Huge ")

sum =0
for i in range (0,500001):
    if (i%2 ==1):
        sum+=i
print(sum)


print("countdown by fours")

for i in range(2018,0, -4):
    print(i)

print("flexible counter")

low_num = 1
high_num = 54
mult = 3

for i in range (low_num,high_num):
    if i % mult ==0:
        print(i)