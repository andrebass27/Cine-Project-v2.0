'''www.practicepython.org'''
from random import choice

file = open('sowpods.txt')
sowpods = file.readlines()
file.close()

print('The word is: %s' %choice(sowpods).strip())