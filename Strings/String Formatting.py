def print_formatted(number):
    w=len((bin(number)).replace("0b",""))
    for i in range(1,number+1):
        #print (str(i).rjust(w,' '),str(oct(i)[2:]).rjust(w,' '),str(hex(i)[2:].upper()).rjust(w,' '),str(bin(i)[2:]).rjust(w,' '))
        print(str(i).rjust(w,' '),str((oct(i).replace("0o",""))).rjust(w,' '),str(((hex(i)).replace("0x","")).upper()).rjust(w,' '),str((bin(i)).replace("0b","")).rjust(w,' '))
       


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
