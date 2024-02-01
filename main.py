# VARIABLES
# Variables are dinamically typed
import math

n=0
print('n= ',n)

# types are assigned during runtime therefore we ca
n='abc'
print('n= ',n)

# Multiple assignment
n,m = 0 ,'abc'

# increment
n=n+1 #good
n+=1 #good
# n++ bad

# None is null (absence of value)

# IF STATEMENT
# there is even elif special keyword
q=1
if q>2:
    q-=1
elif q==2:
    q*=2
else:
    q+=2
# Parantheses needed for multi-line conditions.
# in python && = and
# in python || = or

# LOOPS
# While loop
g=0
while g<5:
    print(g)
    g+=1
# Looping from i=0 to i=4
for b in range(19):
    print(b)
# we can set up a range
# not including 6
for b in range(2,6):
    print(b)
# we can decrement
for b in range(5,1,-2):
    print(b)

# MATH
# Devision
# print(5/2) => 2.5
# pring(5//2) =>2

# IN MOST LANGUAGES WE ARE ROUNDING TOWARDS 0
# IN PYTHON WE ARE ROUNDING DOWN
# print(-3//2) => -2
# In other lagnauges we would receive -1
# to solve this we just need to convert to int
# print(int(-3/2)) =>-1

# Modding
# print(10%3) =>1
# pring(-10%3) => 2 loool

# to get consistent with outher languages
# import math
# print(math.fmod(-10,3)) => -1.0

# More stuff
import math
print(math.floor(3/2)) #round to the higher
print(math.ceil(3/2)) #round to the lover
print(math.sqrt(9))
print(math.pow(2,3)) #2^3

# Max / Min Int
float("inf")
float("-inf")

# There us never overflow like in JS
print(math.pow(2,200)) #and this will print the value

# ARRAYS = In Python is called LISTS
arr=[1,2,3]
arr.append(2)
arr.append(3) #add val to the end
arr.pop() #remove the last val
print(arr)
arr.insert(1,7) #at index 1 we added value 7
print(arr)
arr[0]=0
arr[1]=0
print(arr) #fist 2 val changed to 0

# Initialize arr of suze n with default val of 1
n=5
arr = [1]*n
print(arr)
print(len(arr))
# check last val you can with -1

# Sublists (AKA Slicing)
arr1 = [1,2,3,4]
print(arr[1:3])
# we will receive 2,3 (it is not including last el

# Unpacking (in Js spread)
a,b,c = [1,2,3]
print(a,b,c)

# Looping array
nums = [1,2,3]

# using Index
for i in range(len(nums)):
    print(nums[i])
# Without index
for n in nums:
    print(n)
# Without index and value
for i,n in enumerate(nums):
    print(i,n)

# Loop through multiple arrays simultaneously
# with unpacking
nums1 = [1,3,5]
nums2 = [2,4,6]
# zip will take this 2 arrays and combine these values
for n1,n2 in zip(nums1,nums2):
    print(n1,n2)
# we receive 1 2   3 4   5 6

# Reverse an array
nums = [1,2,3]
nums.reverse()
print(nums)

# SORTING
arr = [5,4,7,435,22,3]
arr.sort()
print(arr)
# in reverse
arr.sort(reverse=True)
print(arr)
arr = ['mike','doe','tony','joe']
arr.sort()
print(arr) #sorted alphabetically
arr.sort(key=lambda x:len(x))
print(arr) #sorted depending on length

# LIST COMPREHENTION
arr = [i for i in range(5)]
print(arr)

# 2D ARRAYS
arr = [[0]*4 for i in range(4)]
print(arr)
# arr = [[0]*4]*4 this will not work as if we modify one value
# then other values also will be modified

# STRINGS
s='abs'
# we can do like with arr
print(s[0:2])
# but they are immutable and you can't do this
# s[0] = "A"

# s+="def" this creates a new string

# Converting into Str/Int
print(int('111')+int('222'))
print(str(111)+str(222))

#Get an ASCII value of a char
print(ord("a"))
print(ord("b"))
# Combine a list of string
word=['he','ll','o']
print("".join(word))

#QUEUES
from collections import  deque

queue = deque()
queue.append(1)
queue.append(2)
print(queue)

queue.popleft()
print(queue)

queue.appendleft(1)
print(queue)

queue.pop()
print(queue)

# HASH SETS - Only unique values
mySet = set()

mySet.add(1)
mySet.add(2)
print(mySet)
# Length
print(len(mySet))

print(1 in mySet)
print(4 in mySet)
mySet.remove(2)

# List to set
print(set([1,2,3]))
# Set comprehention
mySet = {i for i in range(5)}

#HASHMAPS (dict) ALSO NO DUPLICATES
myMap={}
myMap["alex"]=19
myMap["john"]=23
print(myMap)
print(len(myMap))
# Reassign
myMap['alex'] = 22
# checking if the val is in the hashmap
print("alex" in myMap)
# removing
myMap.pop("alex")

#Dictionary comprehention
myMap = {i:2*i for i in range(3)} #extremely convenient
print(myMap)

# Looping through maps
myMap = {"mike":90,"bob":34}
for key in myMap:
    print(key,myMap[key])
for val in myMap.values():
    print(val)
for key,val in myMap.items():
    print(key,val)
# check out output and everything will become obvious

# TUPLES - they are immutable
tup = (1,2,3)

# HEAPS
import heapq

# under the hood they are actually arrays
minHeap=[]
# heapq.heappush(whereToPush,whichValToPush)
heapq.heappush(minHeap,3)
heapq.heappush(minHeap,2)
print(minHeap)

# Min is always at index 0
print(minHeap[0])

while len(minHeap):
    print(heapq.heappop(minHeap))

# By default Python doesn't have max heaps,you can just use min heap
# and then multiply by -1 when push & pop
maxHeap = []
heapq.heappush(maxHeap,-3)
heapq.heappush(maxHeap,-2)
heapq.heappush(maxHeap,-4)

# Max is always at index 0
print(-1 * maxHeap[0])

while len(maxHeap):
    print(-1*heapq.heappop(maxHeap))

# Heap from initial values
arr = [-2,-1,-8,-4,-5]
heapq.heapify(arr)
while arr:
    print(-1*heapq.heappop(arr))

# FUNCTIONS
def myFunc(n,m):
    return n*m
# NESTED FUNCTIONS
# Convenient for Graphs
def outer(a,b):
    c='c'
    def inner():
        return a+b+c
    return inner()

print(outer('a','b'))

# Can modify obj but not reassign but there is a way
# use nonlocal keyword

def double(arr,val):
    def helper():
        #modify arr works
        for i,n in enumerate(arr):
            arr[i] *=2
        # modify only in helper scope
        # val*=2

        # to change actual val use
        nonlocal val
        val *=2
    helper()
    print(arr,val)

double([1,2],3)

# CLASS

class myClass:
    #Constructor
    def __init__(self,nums): #self is like a this keyword
        self.nums = nums

    # Creating methods
    # Self is mandatory even if we don't need parameters
    def getLength(self):
        return self.size
    def getDoubleLen(self):
        return 2*self.getLength()
