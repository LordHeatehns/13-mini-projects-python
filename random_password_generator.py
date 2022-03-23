
import random

input = int(input('length of password\t'))

letter = 'zxcvbnmlkjhgfdsaqwertyuiop0123456789@#$%&ZXCVBNMASDFGHJKLQWERTYUIOP'

password = "".join(random.sample(letter,input))

print(password)