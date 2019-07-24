# Big O notation - A measure of complexity of an algorithm. The worst case scenario of input approaching infinity

########  O(log n) - Logarithmic
######## Binary search - a search on the assorted data
# find the middle element.
# Compare the middle element with the target
# if the target is less than the middle element, upper is mid-1. Recursively call
# if the target is less than the middle element, lower is mid+1.. Recursively call
# Since it is recursive call, base condition is when upper >= lower, the recursion continues


arr  = [ 2, 3, 4, 10, 40 ]
target = 1
print('List to find target ', arr)
print('Target to find ', target)
lower=0
upper= len(arr)-1


def binarySearch(a , t, lower, upper ):

    #base condition for a recursive call
    if upper >= lower:

        mid = lower + int( (upper - lower)/ 2 )

        if a[mid]  == t:
            return mid

        elif a[mid] < t: # go right
            return binarySearch(a , t , mid+1 , upper)

        else:
            return binarySearch(a, t, lower, mid-1 ) # go left
    else:
        return -1

print(binarySearch(arr,target, lower, upper ))

########  O(n log n) -Log Linear






####### O(1)-Constant, O(log n) - Logarithmic are the excellent complexity ranges. O(n)-Linear is a fair range to be in.

####### O(n log n) -Log Linear, O(n**2)-quadratic, O(n**3)- cubic, O(2**n)-Exponential ,O(n!)-Factorial are the horrible complexity ranges to avoid.