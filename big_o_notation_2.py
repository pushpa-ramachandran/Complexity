# Big O notation - A measure of complexity of an algorithm. The worst case scenario of input approaching infinity

########  O(1) - Constant

def example_for_constant(x):
    print(x[0]) #print the first value of the list

example_for_constant([1,2,34])

####### O(n**2) - runtime increases proportional to input n. If n is equal to a million, the runtime increases accordingly
####### when we use nested loops ,the complexity goes up
print(" O(n**2)-Quadratic ")
for n1 in range (1,3):
    for n2 in range(1,11):
        if(n1 == n2):
            print(n1)


####### O(2**n) - exponential - complexity doubles with each increase of n
print(" O(2**n) - exponential ")
####### Finding fibonacci series 0,1,1,2,3,5
'''
if n =0 , output is 0, if n=1 then output is 1. if n > 1 then it is the addition of the 2 previous numbers
'''
def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-2) + fib(n-1)

n=5
print('Recursive approach: ' ,n , 'numbers from the series')

for i in range (0,n):
    print(fib(i))

##### Iterative approach is better than the recursive approach as the time complexity is linear in Iterative.

def fib_i(n):
    if n<=1:
        return n
    else:
        a ,b = 0,1
        for i in range (2,n+1):
            a,b=b,a+b
        return b

n=5
print('Iterative approach: ' ,n , 'numbers from the series')

for x in range(0,n):
    print(fib_i(x))


####### O(1)-Constant, O(log n) - Logarithmic are the excellent complexity ranges. O(n)-Linear is a fair range to be in.

####### O(n log n) -Log Linear, O(n**2)-quadratic, O(n**3)- cubic, O(2**n)-Exponential ,O(n!) are the horrible complexity ranges to avoid.