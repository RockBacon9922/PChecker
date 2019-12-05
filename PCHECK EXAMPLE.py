#Code by Will-bit-tech
import PCheck.PC as PC
length = 8
c = input("PCheck Test: ")
while PC.PC(c, length) == 0 :
    print("password is not sutiable")
    print("Remember the password has to have one capital letter, a number and be longer then " + str(length) + " characters")
    c = input("PCheck Test: ")



