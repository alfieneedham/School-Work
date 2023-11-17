import re

def taskOne(phrase):
    print(re.sub('( )+', ' ', phrase))

def taskTwo(phrase):
    print(re.sub('\d', '*', phrase))

def taskThree(phrase):
    print(re.sub('li[sc]en[sc]e', 'licence', phrase))



def taskA(phrase):
    print(re.sub('[^\d\s]','', phrase))

def taskB(phrase):
    phrase = (re.sub('[iI]','1', phrase))
    phrase = (re.sub('[eE]','3', phrase))
    phrase = (re.sub('[aA]','4', phrase))
    phrase = (re.sub('[sS]','5', phrase))
    phrase = (re.sub('[bB]','8', phrase))
    print(phrase)

def taskC(phrase):
    print(re.sub('[cC](a)+t','KitKat', phrase))

taskOne('Hello         world    !                ')
taskTwo('There are 3 dig1ts in this s3ntence.')
taskThree('This is how you spell licence. Not lisense, license or lisence.')

taskA('Pl3ase r3m0ve 4ll th35e d1gi15.')
taskB('tEsT phRASe fOR reGEx aAbBeEiIsS')
taskC('ct. Cat. caat. Caaaaaaaaat. cAAAAAAAAAAAAAAAAAAAT.')