'''
def celsius_to_fahrenheit(temp):
    return temp * 1.8 + 32.0


print(celsius_to_fahrenheit(10))
'''

s = 'ABC'
for x in s:
    for y in s:
        for z in s:
            if x != y and x != z and y != z:
                print(x, y, z)
                
