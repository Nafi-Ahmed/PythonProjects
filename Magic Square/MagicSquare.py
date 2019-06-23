import numpy as np
# >>prerequisite: numpy package needs to be installed
# >numpy: https://pypi.org/project/numpy/

#  list could be used but it is not recommened as array is faster and efficient
#  While loop prevents wrong inputs, input must be odd integer number
while True:

    try:
        n = int(input("For nxn matrix, enter the value of n: "))
        if n % 2 == 1:
            break
        else:
            print("The number you have entered is Even. Enter an Odd number")
        pass
    except:
        print("Enter a numerical odd number")
        pass


MagicSquare = np.full(n ** 2, None).reshape(n, n)
#  this makes an array of n^2 elements, where each element is None
#  reshape reforms 1d array into 2d array of same row & column,(Square Matrix)


def magic(self):

    # this function arranges numbrs from 1 to n^2 in magic square formation

    # >>here self is used to permanently transform the array given as input.
    itr = np.size(self)

    r = 0
    c = len(self) // 2

    #  this is where the magic happens.
    for elem in range(1, itr + 1):

        if r == -1 and c == n:
            r = 1
            c = n - 1
        elif r == -1:
            r = n - 1

        elif c == n:
            c = 0

        elif self[r, c] != None:
            r += 2
            c -= 1

        self[r, c] = elem

        r -= 1
        c += 1

'''
def check(self):

    # >>checks if the sum of each of the rows, columns and diagonals are equal.
    rng = len(self)

    chk = 1
    val = np.sum(self[rng - 1])

    for row in range(rng):
        c_sum = 0

        for col in range(rng):
            c_sum += self[col, row]

        if np.sum(self[row]) == val and c_sum == val:
            chk *= 1
        else:

            chk *= 0

    a_sum = 0
    b_sum = 0
    b = rng - 1

    for e in range(rng):
        a_sum += self[e, e]

        b_sum += self[e, b - e]
    if a_sum == val and b_sum == val:
        chk *= 1

    else:

        chk *= 0
    if chk == 1:
        print("It is a Magic Square")
    else:
        print("It is Not a Magic Square")


'''
# remove above comment to enable check function
def Print(self):
    # this function only removes brackets,'['&']'
    print("Magic Square of", n, "x", n, "Matrix")
    print(str(self).replace("[", " ").replace("]", " "))


magic(MagicSquare)
Print(MagicSquare)
#check(MagicSquare)
