PChecker by Will-bit-tech 2019

PChecker is used to check a string of characters if they comply with standard secure password practices.
This could be used to make sure uses create a secure password for a program of system
This program only needs one while loop to work.

First copy the PCheck Folder into your program library
Next import the library into your program with the import command e. g import PC
Nice Next create a while loop. We are going to need to put PC.PC() into the while loop here is an example.
I will put this code in "2ndPCheckerExample" which is included in the same directory as this document.

import PCheck.PC as PC
a = input("input ")
b = 7 #required length of password
while PC.PC(a, b) == 0:
	print("password is not good enough")
	a = input("input ")
print("success password matches criteria")

A is a string variable which could be swapped out with whatever your password variable is.
B is an integer which allows you to set the required length of the users password

If you have got this far without error, I congratulate you well done we are finished. If you can please credit me in your final project.
Other than that thank you for using my library!!!

