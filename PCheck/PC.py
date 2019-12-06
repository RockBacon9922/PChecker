#Program By Will-bit-tech
""" Program Wants to know the password (c) and required length
                of the password"""

def PC(c, b):
    
    truee = 0

    trueee = 0

    listthing = list(c)

    lenthlist = len(listthing)

    """Logic for Checking for Capital Letters and Numbers"""
    
    for x in listthing:
        if x >= 'A' and x <= 'Z':
            truee = 1
        if x >= '0' and x <= '9':
            trueee = 1

    """Collecting Results and returning to main program the
    findings of the result"""
            
    if truee == 1 and trueee == 1 and lenthlist >= b:
        return 1
    else:
        return 0

        
