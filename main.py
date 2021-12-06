import random
ford = ['mondeo', 'focus', 'kuga']
fiat = ['tipo', 'panda', '500']
renault = ['clio', 'megan', 'duster']

t = 0

while t not in ['exit', 'Exit']:
    t = input()
    if t == 'ford':
        print(random.choice(ford))
    elif t == 'fiat':
        print(random.choice(fiat))
    elif t == 'renault':
        print(random.choice(renault))
    elif t != ['ford' or 'fiat' or 'renault']:
        print('unknown value')



