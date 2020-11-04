import os
import random
from termcolor import colored
from time import sleep
from Art.art import *

print()

#----Face Art----

DOB=input("Enter Date of Birth")

if DOB=='05/11/1988' or DOB=='5/11/1988' or DOB=='05-11-1988' or DOB=='5-11-1988':
	input("Enter Ctrl+- 7 times & Press Enter")
	for i in range(len(face)):
		print(face[i],sep='', end='',flush= True);sleep(.000000000000000002)
	
else:
	print("Wrong DOB")




