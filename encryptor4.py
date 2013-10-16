# This program will encrypt a text file using a unique seed.
# EDIT: now encrypts everything instead of just alpha characters!

import sys
import random
from datetime import datetime
import zlib, base64

def main():
    seed = 0
    charList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    numList = ['1','2','3','4','5','6','7','8','9','0']

    fileName = raw_input('Enter the name of the file to use: ')
    file = open(fileName,'r')
    string = file.read()
    file.close()

    choice = raw_input("Would you like to enter your own seed? (y/n)")
    if choice == 'n' or choice == 'N':
        seed = random.randint(111111111,9999999999999999)
    if seed == 0:
        seed = raw_input("Please enter the encryption seed: ")

    startTime = datetime.now()

    encryptList = {'1': dig_one,'2': dig_two,'3': dig_three,'4': dig_four,'5': dig_five,'6': dig_six,'7': dig_seven,'8': dig_eight,'9': dig_nine,'0': dig_zero}

    seed = str(seed)
    temp = ''
    for i in range(len(seed)):
        if seed[i] in charList:
            temp += str(ord(seed[i]))
        elif seed[i] in numList:
            temp += seed[i]

    seed = temp
    print(seed)
    for i in range(len(seed)):
        string = encryptList[seed[i]](string,seed)
    code = base64.b64encode(zlib.compress(string,9))

##    outArray = ""
##    for i in range(0,len(code),2):
##        group = code[i:i+2]
##        plain_number = ord(group[0])*256+ord(group[1])
##        encrypted = pow(plain_number,8,37329)
##        outArray += """
##"""+str(encrypted)
##        print group,"-->",plain_number,"-->",encrypted
    
    file = open(fileName,'w')
    file.write(code)
    file.close()
    print("Wrote to file.")

    endTime = datetime.now()
    print(endTime-startTime)

def dig_one(string,seed):
    outStr = ''
    for i in range(len(string)):
        temp = ord(string[i])
        temp+= 5
        if temp>=256:
            temp-=256
        outStr += chr(temp)
    return(outStr)

def dig_two(string,seed):
    outStr = ''
    for i in range(len(string)):
        if i%2==0 and i!=0:
            outStr+= string[i]
            outStr+= string[i-1]
        elif i == 0:
            outStr+= string[i]
        elif i%2==1 and i == len(string)-1:
            outStr+= string[i]
    return(outStr)

def dig_three(string,seed):
    outStr = ''
    beginStr = string[:(eval(seed[2]))]
    endStr = string[(eval(seed[2])):]
    outStr+=endStr
    outStr+=beginStr
    return(outStr)

def dig_four(string,seed):
    outStr = ''
    beginStr = string[:(len(string)-eval(seed[3]))]
    endStr = string[(len(string)-eval(seed[3])):]
    outStr+=endStr
    outStr+=beginStr
    return(outStr)

def dig_five(string,seed):
    outStr = ''
    for i in range(len(string)):
            temp = ord(string[i])
            temp-= 3
            if temp<0:
                temp+=256
            outStr += chr(temp)
    return(outStr)

def dig_six(string,seed):
    outStr = ''

    tempStrs = []
    for i in range(len(string)):
        if i%4==0 and i<=len(string)-4:
            tempStrs.append(string[i:i+4])
        elif i%4==0 and i>len(string)-4:
            tempStrs.append(string[i:])

    for i in range(len(tempStrs)):
        if len(tempStrs[i])==4:
            tempChar0 = tempStrs[i][0]
            tempChar2 = tempStrs[i][2]

            tempStr = ''
            tempStr+=tempChar2
            tempStr+=tempStrs[i][1]
            tempStr+=tempChar0
            tempStr+=tempStrs[i][3]
        else:
            tempStr = tempStrs[i]
        outStr+= tempStr
    
    return(outStr)

def dig_seven(string,seed):
    outStr = ''
    tOutStr = ''
    tempList = string.split(' ')
    for i in range(len(tempList)):
        tempStr = ''
        for j in range(len(tempList[i])):
            tempStr += tempList[i][len(tempList[i])-(j+1)]
        tOutStr += tempStr
        tOutStr += ' '
    for i in range(len(tOutStr)):
        if i!=(len(tOutStr)-1):
            outStr+= tOutStr[i]
    return(outStr)

def dig_eight(string,seed):
    outStr = ''
    for i in range(len(string)):
        if seed[1]!='0':
            if i%eval(seed[1])==0:
                temp = ord(string[i])
                temp+= eval(seed[5])
                if temp>=256:
                    temp-=256
                outStr += chr(temp)
            else:
                outStr += string[i]
        else:
            if i%2==0:
                temp = ord(string[i])
                temp-= eval(seed[5])
                if temp<0:
                    temp+=256
                outStr += chr(temp)
            else:
                outStr += string[i]
    return(outStr)

def dig_nine(string,seed):
    return(string)

def dig_zero(string,seed):
    outStr = ''
    if int(seed[1])!=0:
        for i in range(len(string)):
            if i%int(seed[1])==0:
                outStr += chr(random.randint(32,33))
                outStr += string[i]
            else:
                outStr += string[i]
    return(outStr)

main()
