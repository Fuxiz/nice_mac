import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--upper",dest ="uppercase", default="-l", help="Uppercase")
parser.add_argument("-l", "--lower",dest = "lowercase", default="-l",help="Lowercase")
parser.add_argument('text', action='store', type=str, help='The text to parse.')
args = parser.parse_args()


mac2 = list(args.text.replace('.','').replace(':','').replace('-',''))
cleanmac = mac2.copy();print("".join(cleanmac).lower())
charlist = [[":","-","-",".","."],[2, 5, 8, 11, 14],[6],[4,9],[2, 5, 8, 11, 14],[4,9]]
for listpos in range(0,len(charlist)-1):     #Loops through every list
    m = listpos; listpos+=1                       #while g steps through each list it also steps through each character
    for i in range(0,len(charlist[listpos])):       #looks up and loops the amount of character in the list 
        mac2.insert(charlist[listpos][i], charlist[0][m])  #inserts all the character in the list and in the the position of the lists.
    print("".join(mac2))     
    mac2 = cleanmac.copy()   # Clears for new characters
print('\n')
