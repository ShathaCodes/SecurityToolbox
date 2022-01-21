import math

from tools import prime_check, pgcd, verify_primary_numbers, calculate_d

listOfSymbols = ['0', '1', '2', '3', '4', '5',
                 '6', '7', '8', '9', ' ', '!', '.', '?', '#']


def calcule_e(p,q):    
    n=p*q
    phi=(p-1)*(q-1)
    '''CALCULATION OF 'e'.'''
    for i in range(1, 1000):
        if(verify_primary_numbers(i, phi) == 1):
            e = i
    public = (e, n)
    print("Public Key =", public)
    return (n,phi,e)

def calcule_d(p,q):
    result=calcule_e(p,q)
    n=result[0]
    phi=result[1]
    e=result[2]
    
    pgcd(e, phi)
    d = calculate_d(e, phi)

    #public = (e, n)
    private = (d, n)
    print("Private Key =", private)
    
    return(d,n,e)

# Encryption
'''ENCRYPTION ALGORITHM.'''


def encrypt(pub_key, n_text):
    test = False
    e, n = pub_key
    x = []
    m = 0
    for i in n_text:
        test = False
        for symbol in listOfSymbols:
            if (i == symbol):
                test = True
        if(test):
            x.append(400+listOfSymbols.index(i))
        else:
            if(i.isupper()):
                m = ord(i)-65
                c = (m**e) % n
                x.append(c)
            elif(i.islower()):
                m = ord(i)-97
                c = (m**e) % n
                x.append(c+27)
    return x


# Decryption
'''DECRYPTION ALGORITHM'''


def decrypt(priv_key, c_text):
    d, n = priv_key
    txt = c_text.split(',')
    x = ''
    m = 0
    for i in txt:
        if(int(i) >= 400):
            x += listOfSymbols[(int(i)-400)]
        else:
            if (int(i) >= 27):
                m = ((int(i)-27)**d) % n
                m += 97
                c = chr(m)
                x += c
            else:
                m = (int(i)**d) % n
                m += 65
                c = chr(m)
                x += c
    return x

