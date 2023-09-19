print('welcome to blackjack or 21 if you prefer')
print(end='\n')

end = 1
#randomize a number
import random
n = random.randint(1, 11)
print('you got a', n,)

import random
a = random.randint(1, 10)
print('and you got a', a,)
print(end='\n')

#this is how many you got in total
black = a + n
print('all together you got', black,)

#this are the conditions
if black == 21:
    print('you win the game!')

if black < 21:
    input('you can draw with "draw" or stop right there with "stop"')

if black > 21:
    print('you lost the game...')

while end == 1:
    if black == 21:
        end = 0
    if black > 21:
        end = 0
