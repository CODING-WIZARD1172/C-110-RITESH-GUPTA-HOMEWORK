import random


droll = 'a'


def diceNo(n):
    if n == 1:
        print('[       ]')
        print('[   *   ]')
        print('[       ]')
    elif n == 2:
        print('[ *     ]')
        print('[       ]')
        print('[     * ]')
    elif n == 3:
        print('[ *     ]')
        print('[   *   ]')
        print('[     * ]')
    elif n == 4:
        print('[ *   * ]')
        print('[       ]')
        print('[ *   * ]')
    elif n == 5:
        print('[ *   * ]')
        print('[   *   ]')
        print('[ *   * ]')
    elif n == 6:
        print('[ *   * ]')
        print('[ *   * ]')
        print('[ *   * ]')
    else:
        print('SOME ERROR OCCURED')


while droll == 'a':
    x = random.randint(1, 6)
    diceNo(x)
    droll = (input('ENTER A TO ROLL DICE AND Q TO QUIT :  ')).lower()
