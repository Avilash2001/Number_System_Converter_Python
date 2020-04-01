def dec_to_bin():
    arr=[]
    #We create an array and store every degit individually
    num=int(input("Enter the decimal number: "))
    i=0
    #We store the remainder in them as we did in paper using long division
    while num!=0:
        t=num%2
        arr.append(t)
        num=int(num/2)
        i=i+1
    print("The binary number is: ")
    j=i-1
    while j>=0:
        print(arr[j],end="")
        j=j-1
def dec_to_oct():
    arr=[]
    #We create an array and store every degit individually
    num=int(input("Enter the decimal number: "))
    i=0
    #We store the remainder in them as we did in paper using long division
    while num!=0:
        t=num%8
        arr.append(t)
        num=int(num/8)
        i=i+1
    print("The octal number is: ")
    j=i-1
    while j>=0:
        print(arr[j],end="")
        j=j-1
def dec_to_hex():
    arr=[]
    #We create an array and store every degit individually
    num=int(input("Enter the decimal number: "))
    i=0
    #We store the remainder in them as we did in paper using long division
    while num!=0:
        t=num%16
        arr.append(t)
        num=int(num/16)
        i=i+1
    print("The hexadecimal number is: ")
    j=i-1
    while j>=0:
        if arr[j] == 10:
            print("A",end="")
        elif arr[j] == 11:
            print("B",end="")
        elif arr[j] == 12:
            print("C",end="")
        elif arr[j] == 13:
            print("D",end="")
        elif arr[j] == 14:
            print("E",end="")
        elif arr[j] == 15:
            print("F",end="")
        else:
            print(arr[j],end="")
        j=j-1
def bin_to_dec():
    num=int(input("Enter the binary number: "))
    i=0
    r=0
    #We go on multiplieng individual numbers by increasing power of 2 as we do in copy
    while num!=0:
        t = num % 10
        r=r+t*(2**i)
        num = int(num/10)
        i=i+1
    print("The decimal number: "+str(r))
def bin_to_oct():
    arr=[]
    #First we convert the binary number to decimal
    num=int(input("Enter the binary number: "))
    i=0
    r=0
    while num!=0:
        t = num % 10
        r=r+t*(2**i)
        num = int(num/10)
        i=i+1
    num1=r
    #Now we convert the Decimal number to octal
    z=0
    while num1!=0:
        t=num1%8
        arr.append(t)
        num1=int(num1/8)
        z=z+1
    print("The octal number is: ")
    j=z-1
    while j>=0:
        print(arr[j],end="")
        j=j-1
def bin_to_hex():
    arr=[]
    #First we convert the binary number to decimal
    num=int(input("Enter the binary number: "))
    i=0
    r=0
    while num!=0:
        t = num % 10
        r=r+t*(2**i)
        num = int(num/10)
        i=i+1
    num1=r
    #Now we convert the Decimal number to hexa decimal
    z=0
    while num1!=0:
        t=num1%16
        arr.append(t)
        num1=int(num1/16)
        z=z+1
    print("The hexadecimal number is: ")
    j=z-1
    while j>=0:
        if arr[j] == 10:
            print("A",end="")
        elif arr[j] == 11:
            print("B",end="")
        elif arr[j] == 12:
            print("C",end="")
        elif arr[j] == 13:
            print("D",end="")
        elif arr[j] == 14:
            print("E",end="")
        elif arr[j] == 15:
            print("F",end="")
        else:
            print(arr[j],end="")
        j=j-1
def oct_to_dec():
    num=int(input("Enter the octal number: "))
    i=0
    r=0
    #We go on multiplieng individual numbers by increasing power of 8 as we do in copy
    while num!=0:
        t = num % 10
        if t>= 8:
            print("\nInvalid input octal cannot have symbols more than 7\n")
        else:
            r=r+t*(8**i)
            num=int(num/10)
            i=i+1
    print("The decimal number: "+str(r))
def oct_to_bin():
    arr=[]
    #first we convert the octal number to decimal
    num=int(input("Enter the octal number: "))
    i=0
    r=0
    while num!=0:
        t = num % 10
        if t>= 8:
            print("\nInvalid input octal cannot have symbols more than 7\n")
        else:
            r=r+t*(8**i)
            num=int(num/10)
            i=i+1
    num1=r
    #Then we convert the decimal number to Binary
    z=0
    while num1!=0:
        t=num1%2
        arr.append(t)
        num1=int(num1/2)
        z=z+1
    print("The binary number is: ")
    j=z-1
    while j>=0:
        print(arr[j],end="")
        j=j-1
def oct_to_hex():
    arr=[]
    num=int(input("Enter the octal number: "))
    i=0
    r=0
    #first we convert the octal to decimal
    while num!=0:
        t = num % 10
        if t>= 8:
            print("\nInvalid input octal cannot have symbols more than 7\n")
        else:
            r=r+t*(8**i)
            num=int(num/10)
            i=i+1
    num1=r
    #Then we convert the decimal number to hexadecimal
    z=0
    while num1!=0:
        t=num1%16
        arr.append(t)
        num1=int(num1/16)
        z=z+1
    print("The hexadecimal number is: ")
    j=z-1
    while j>=0:
        if arr[j] == 10:
            print("A",end="")
        elif arr[j] == 11:
            print("B",end="")
        elif arr[j] == 12:
            print("C",end="")
        elif arr[j] == 13:
            print("D",end="")
        elif arr[j] == 14:
            print("E",end="")
        elif arr[j] == 15:
            print("F",end="")
        else:
            print(arr[j],end="")
        j=j-1

def hex_to_dec():
    num=input("Enter the hexadecimal number: ")
    num=list(num)
    c=0
    r=0
    j=0
    while j<len(num):
        c=c+1
        j=j+1
    c=c-1
    i=0
    while i<len(num):
        #we chage the char values to thier integer values
        if num[i] >= '0' and num[i] <='9':
            t=ord(num[i])-48
        elif num[i] >= 'A' and num[i] <='F':
            t=ord(num[i])-65+10
        #We go on multiplieng individual numbers by increasing power of 16 as we do in copy
        r=r+t*(16**c)
        c=c-1
        i=i+1
    print("The decimal number: "+str(r))
def hex_to_bin():
    arr=[]
    num=input("Enter the hexadecimal number: ")
    num=list(num)
    c=0
    r=0
    j=0
    #we change the number from hexadecimal to decimal
    while j<len(num):
        c=c+1
        j=j+1
    c=c-1
    i=0
    while i<len(num):
        if num[i] >= '0' and num[i] <='9':
            t=ord(num[i])-48
        elif num[i] >= 'A' and num[i] <='F':
            t=ord(num[i])-65+10
        r=r+t*(16**c)
        c=c-1
        i=i+1
    num1=r
    #now we change the decimal number to binary
    z=0
    while num1!=0:
        t=num1%2
        arr.append(t)
        num1=int(num1/2)
        z=z+1
    print("The binary number is: ")
    j=z-1
    while j>=0:
        print(arr[j],end="")
        j=j-1
def hex_to_oct():
    arr=[]
    num=input("Enter the hexadecimal number: ")
    num=list(num)
    #we change the number from hexadecimal to decimal
    c=0
    r=0
    j=0
    while j<len(num):
        c=c+1
        j=j+1
    c=c-1
    i=0
    while i<len(num):
        if num[i] >= '0' and num[i] <='9':
            t=ord(num[i])-48
        elif num[i] >= 'A' and num[i] <='F':
            t=ord(num[i])-65+10
        r=r+t*(16**c)
        c=c-1
        i=i+1
    num1=r
    #Now we change the decimal to octal 
    z=0
    while num1!=0:
        t=num1%8
        arr.append(t)
        num1=int(num1/8)
        z=z+1
    print("The octal number is: ")
    j=z-1
    while j>=0:
        print(arr[j],end="")
        j=j-1
def main():
    run=1
    print("\nThis is a software created to convert one number system to another\n")
    print("\n Every number system has a base or radix which is the total number of symbols in that number system.\n")
    #We will run the loop till this variable is one and we will change the value when we want to end the loop.
    while run!=0:
        print("These are the bases of the most commonly used number system.\n\n1. Decimal = 10\n2. Binary = 2")
        print("3. Octal = 8\n4. Hexadecimal = 16\n")
        #Here we ask the user to input the base of the given and required base
        base1=int(input("\nEnter the base of the given number system: \n"))
        base2=int(input("\nEnter the base of the required number system: \n"))
        #now we will evaluate different cases for different values of base1 and base2
        if base1 == 10:
            #This will evaluate all the cases of decimal
            if base2 == 2:
                #This will convert to decimal to binary
                dec_to_bin()
                choice=input("\nDo you want to use the software again? \n")
                if choice == 'N' or choice == 'n':
                    run = 0
            elif base2 == 8:
                #This will convert to decimal to octal
                dec_to_oct()
                choice=input("\nDo you want to use the software again? \n")
                if choice == 'N' or choice == 'n':
                    run = 0
            elif base2 == 16:
                #This will convert to decimal to hexadecimal
                dec_to_hex()
                choice=input("\nDo you want to use the software again? \n")
                if choice == 'N' or choice == 'n':
                    run = 0
        elif base1 == 2:
            #This will list all cases of binary
            if base2 == 10:
                #This will convert binary to decimal
                bin_to_dec()
                choice=input("\nDo you want to use the software again? \n")
                if choice == 'N' or choice == 'n':
                    run = 0
            elif base2 == 8:
                #This will convert to binary to octal
                bin_to_oct()
                choice=input("\nDo you want to use the software again? \n")
                if choice == 'N' or choice == 'n':
                    run = 0
            elif base2 == 16:
                #This will convert to binary to hexadecimal
                bin_to_hex()
                choice=input("\nDo you want to use the software again? \n")
                if choice == 'N' or choice == 'n':
                    run = 0
        elif base1 == 8:
            #This will list all cases of octal
            if base2 == 10:
                #This will convert octal to decimal
                oct_to_dec()
                choice=input("\nDo you want to use the software again? \n")
                if choice == 'N' or choice == 'n':
                    run = 0
            elif base2 == 2:
                #This will convert octal to binary
                oct_to_bin()
                choice=input("\nDo you want to use the software again? \n")
                if choice == 'N' or choice == 'n':
                    run = 0
            elif base2 == 16:
                #This will convert octal to hexadecimal
                oct_to_hex()
                choice=input("\nDo you want to use the software again? \n")
                if choice == 'N' or choice == 'n':
                    run = 0
        elif base1 == 16:
            #This will list all cases of hexadecimal
            if base2 == 10:
            #This will convert hexadecimal to decimal
                hex_to_dec()
                choice=input("\nDo you want to use the software again? \n")
                if choice == 'N' or choice == 'n':
                    run = 0
            elif base2 == 2:
                #This will convert hexadecimal to binary
                hex_to_bin()
                choice=input("\nDo you want to use the software again? \n")
                if choice == 'N' or choice == 'n':
                    run = 0
            elif base2 == 8:
                #This will convert hexadecimal to octal
                hex_to_oct()
                choice=input("\nDo you want to use the software again? \n")
                if choice == 'N' or choice == 'n':
                    run = 0
main()