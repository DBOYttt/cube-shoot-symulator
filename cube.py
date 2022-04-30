import imp


import random

print('hi im tobi beta function')



while 1:

    x = input('can we start?(yes or no):')

    if x == 'yes':
        y = random.randint(1, 6)
    if y == 1:
        print("""
    -------
    |  o  |
    -------
    """) 
    elif y == 2:
        print("""
    -------
    | o o |
    -------
    """)
    elif y == 3:
        print("""
    ---------
    | o o o |
    ---------
    """)
    elif y == 4:
        print("""
    -----------
    | o o o o |
    -----------
    """)
    elif y == 5:
        print("""
    ------------
    | o o o o o |
    ------------
    """)



