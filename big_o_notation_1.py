# Big O notation - A measure of complexity of an algorithm

# O(1) - Constant

####### O(n) - runtime increases proportional to input n. If n is equal to a billion, the runtime increases accordingly
n = 10
sum = 0

for i in range(1,n+1):
    print (sum)
    sum+= i

print(sum)


######## How to improve O(n) in the above example

n = 50
sum = 0

# use of simple formula reduced the assignments needed and hence reduces the overall runtime
sum = n * (n+1)/2

print(sum)


#######O(n**y)

# Consider a non-linear equation -  X**3 + X**2 + X + 1
# The runtime of this equation is largely determined by X**3 and hence the complexity is Cubic

X = 2
result =  X**3 + X**2 + X + 1

print(result)


####### O(1)-Constant, O(log n) - Logarithmic are the excellent complexity ranges. O(n)-Linear is a fair range to be in.

####### O(n log n) -Log Linear, O(n**2)-quadratic, O(n**3)- cubic, O(2**n)-Exponential ,O(n!) are the horrible complexity ranges to avoid.