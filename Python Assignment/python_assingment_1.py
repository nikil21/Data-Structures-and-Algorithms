#question 1(a):
def sum_of_sqaures(n):
    sum = 0
    for i in range(1,n):
        sum += i*i
    return(sum)

#question 1(b):
def sum_of_sqaures_odd(n):
    sum = 0
    for i in range(1,n,2):
        sum += i*i
    return(sum)


#question 2(a):        
range(60,90,10)

#question 2(b):
range(-4,6,2)

#question 3:
def prod_odd(ar):
    for i in range(len(ar)-1):
        for j in range(i+1,len(ar)):
            if ((ar[i]*ar[j]) % 2 != 0):
                print(ar[i],ar[j])
   
#question 4:
def count_vowels(s):
    s = list(s)
    count = 0
    vowels = ['a','e','i','o','u']
    for vowel in vowels:
        if vowel in s:
            count += 1
    
            
#question 5:    
a, b, c = [int(x) for x in input("Enter three value: ").split()]

if a+b == c:
    print('yes they can be used in a+b=c')
if a == b-c:
    print('yes they can be used in a=b-c')
if a*b == c:
    print('yes they can be used in a*b=c')
    


#question 6:
#Design a program that can test the Birthday problem, by a series of experiments, on randomly generatedbirthdays which test this paradox for n = 5,10,15,20,25,30...200
import math
import matplotlib.pyplot as plt
import numpy as np


def make_birthday_list(count):
    return np.random.randint(1,366,count)

def duplicates(the_list):
    return len(the_list)!=len(set(the_list))

num_samples = 10000
for count in range(100):
    dup = 0
    for test_number in range(num_samples):
        the_list = make_birthday_list(count)
        if duplicates(the_list):
            dup += 1
    print(count, dup/num_samples)
    plt.scatter(count, dup/num_samples)



# Returns approximate number of people for a given probability p
def find( p ): 
    return math.ceil(math.sqrt(2 * 365 *
                     math.log(1/(1-p))));