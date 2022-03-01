import string
import os
import numpy


howmanycodes = int(input('How many codes you want to generate: '))
chars = []
chars[:0] = string.ascii_letters + string.digits
c = numpy.random.choice(chars, size=[howmanycodes, 23])
cds = []
for s in c:  # Loop over the amount of codes to check
    code = ''.join(x for x in s)
    url = f"{code}"  # Generate the url
    print(url + ' writing in codes.txt')
    cds.append(url)
    with open('codes.txt', 'a') as f:
        f.write(str(url) + '\n')
input('Generated '+str(howmanycodes)+' codes!')
