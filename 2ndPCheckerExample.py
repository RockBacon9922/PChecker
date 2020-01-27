#Code by Will-bit-tech
import PCheck.PC as PC
a = input("input ")
b = 7 #required length of password
while PC.PC(a, b) == False:
	print("password is not good enough")
	a = input("input ")
print("success password matches criteria")
