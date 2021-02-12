import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--upper",dest ="uppercase", default="-l", help="Print mac addresses in uppercase",action='store_true')
parser.add_argument("-l", "--lower",dest = "lowercase", default="-l",help="Print mac addresses in lowercase",action='store_true')
parser.add_argument('mac', action='store', type=str, help='Mac address',nargs='*')
args = parser.parse_args()
print(args.mac)
print(args.uppercase)

for item in args.mac:
    print(item)
    mac2 = list(str(item).replace('.','').replace(':','').replace('-',''))
    cleanmac = mac2.copy();print("".join(cleanmac).lower())
    charlist = [[":","-","-",".","."],[2, 5, 8, 11, 14],[6],[4,9],[2, 5, 8, 11, 14],[4,9]]
    for listpos in range(0,len(charlist)-1):     #Loops through every list
        m = listpos; listpos+=1                       #while g steps through each list it also steps through each character
        for i in range(0,len(charlist[listpos])):       #looks up and loops the amount of character in the list 
            mac2.insert(charlist[listpos][i], charlist[0][m])  #inserts all the character in the list and in the the position of the lists.
        if args.uppercase is not True:
            print("".join(mac2))
        else:
            print("".join(mac2).upper())
        mac2 = cleanmac.copy()   # Clears for new characters
    print('\n')
