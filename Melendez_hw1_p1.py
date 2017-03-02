integer = int(input('Please enter the desired integer: '))
num = integer
binary=[]

while(integer > 0):
    a=int(float(integer%2))
    binary.append(a)
    integer = (integer - a)/ 2
binary.append(0)

string=""

for j in binary[::-1]:
    string += str(j)

print('The integer', num, 'is expressed as', string, 'in binary')