# Problem 1

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.
#print ("hello world")


# make a list of all the numbers below 1000
# get the multiples of 3, 5 below 1000
# for every number in the list devide it by 3 or 5
# add the ones that are not decimals together for the sum
#
a = [1,2,3,4,5,6,12]
for i in a: 
    
    print ("mod 3:",i%3) 
    print ("mod 5:",i%5)
b=list (range(1,1001))
print (b)

