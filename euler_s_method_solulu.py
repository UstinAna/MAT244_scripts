# Jan 22nd, 2025
# Author: Austin Hua

def e6_f(x, y):
    return 3 *x ** 2 / (3 * y ** 2 - 4)

def e5_f(x, y):
    return 2 *x + y

def x(x0, h):
    return x0 + h

def y(x0, y0, h, q):
    '''
    post: integer
    '''
    if q == 'e6':
        return y0 + e6_f(x0, y0) * h
    elif q == 'e5':
        return y0 + e5_f(x0, y0) * h
    else:
        return None

def e6b_solulu():
    print('__________________')
    print('e6 part b solulu: ')
    y0 = 0
    x0 = 1
    h = 0.05
    for i in range(16):
        x0 = float(int(x(x0, h) * 100)/ 100)
        y0 = y(x0, y0, h, 'e6')
        if x0 == 1.2 or x0 == 1.4 or x0 == 1.6 or x0 == 1.8:
            print(x0, '|', float(int(y0 * 1000))/ 1000)

def e6a_solulu():
    print('__________________')
    print('e6 part a solulu: ')
    y0 = 0
    x0 = 1
    h = 0.1
    for i in range(16):
        x0 = float(int(x(x0, h) * 10)/ 10)
        y0 = y(x0, y0, h, 'e6')
        if x0 == 1.2 or x0 == 1.4 or x0 == 1.6 or x0 == 1.8:
            print(x0, '|', float(int(y0 * 1000))/ 1000)

def e5_solulu():
    print('__________________')
    print('e5 solulu: ')
    y0 = 1
    x0 = 0
    h = 0.1
    for i in range(15):
        x0 = x(x0, h)
        y0 = y(x0, y0, h, 'e5')
        print(float(int(x0 * 10))/ 10, '|', float(int(y0 * 1000))/ 1000)

if __name__ == "__main__":
    while True:
        question = input('which question are we solving? (e5, e6, e6a, e6b): ').lower()
        match question:
            case 'e5':
                e5_solulu()
            case 'e6a':
                e6a_solulu()
            case 'e6b':
                e6b_solulu()
            case 'e6':
                e6a_solulu()
                e6b_solulu()
            case 'exit':
                break
            case _:
                continue