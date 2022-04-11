# Write a function that returns the lesser of two given numbers if both numbers are even, 
# but returns the greater if one or both numbers are odd

def lesserOfTwoEvens(a,b):
    if a % 2 == 0 and b % 2 == 0:
        if a<b:
            return a
        return b
    else:
        if a > b:
            return a
        return b

print(lesserOfTwoEvens(2,4))
print(lesserOfTwoEvens(10,30))



# Write a function takes a two-word string and 
# returns True if both words begin with same letter
def animalCracker(string):
    x = string.split()
    if x[0][0] == x[1][0]:
        return True
    return False

print(animalCracker('Levelheaded Llama'))
print(animalCracker('Crazy Kangaroo'))



# Given two integers, return True if the sum of the integers is 20 
# or if one of the integers is 20. If not, return False
def makesTwenty(n1,n2):
    if n1 == 20 or n2 == 20:
        return True
    elif n1 + n2 == 20:
        return True
    return False

print(makesTwenty(20,10))
print(makesTwenty(12,8))
print(makesTwenty(2,3))



# Write a function that capitalizes the first and fourth letters of a name..
def caps(string):
    g = ''
    for i,j in enumerate(string):
        if i == 0 or i == 3:
            g += j.upper()
        else:
            g += j
    return g

print(caps('macdonald'))



# Given a sentence, return a sentence with the words reversed
def masterYoda(st):
    x = st.split()
    return " ".join(x[::-1])

print(masterYoda('I am Home'))
print(masterYoda('We are ready'))



# Given an integer n, return True if n is within 10 of either 100 or 200
def almostThere(n):
    if n in range(90,111) or n in range(190, 211):
        return True
    return False

print(almostThere(190))
print(almostThere(109))
print(almostThere(150))
print(almostThere(210))
print(almostThere(179))


#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
def has33(nums):
    for i in range(0, len(nums)):
        if(i+1 < len(nums)):
            if(nums[i] == 3 and nums[i+1] == 3):
                return True
    return False

has33([3,3,1,2,4])
- True
has33([1,3,3])
- True
has33([1,3,1,3])
- False
has33([3,1,3])
- False


# Given a string, return a string where for every character 
# in the original there are three characters
def paperDoll(text):
    g = []
    for i in text:
        g.append(i*3)
    return ''.join(g)

paperDoll('Hello')
-'HHHeeellllllooo'
paperDoll('Mississippi')
-'MMMiiissssssiiissssssiiippppppiii'


# SUMMER OF '69: Return the sum of the numbers in the array, 
# except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). 
# Return 0 for no numbers.
def summer69(lst):
    it = iter(lst)
    total = 0
    for x in it:
        if x == 6:
            9 in it
        else:
            total += x
    return total

summer69([1,2,3,4,5,6,7,8,9])
15
summer69([1,3,5])
9
summer69([4,5,6,7,8,9])
9
summer69([2,1,6,9,11])
14


# COUNT PRIMES: Write a function that returns the number of prime numbers 
# that exist up to and including a given number
def checkPrime(num):
    count = 0
    for n in range(2, num+1):
        flag = False
        for i in range(2, n):
            if(n % i == 0):
                flag = True
                break
        if flag==False:
            count += 1
    return count

checkPrime(100)
25
checkPrime(1000)
168
checkPrime(10000)
1229
checkPrime(100000)
9592


#BANK PROBLEM
def accounts():
    age = int(input('Enter you age: '))
    dep = int(input('Enter deposite amount: '))
    if( dep >= 100 ):
        if( age >= 21 ):
            return 'TYPE A'
        return "TYPE B"
    else:
        if( age >= 21):
            return 'TYPE C'
        return 'DO NOT DEPOSITE'
accounts()
Enter you age: 30
Enter deposite amount: 100
'TYPE A'
accounts()
Enter you age: 16
Enter deposite amount: 200
'TYPE B'
accounts()
Enter you age: 18
Enter deposite amount: 90
'DO NOT DEPOSITE'
accounts()
Enter you age: 26
Enter deposite amount: 80
'TYPE C'
