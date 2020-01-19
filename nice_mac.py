import sys
mac2 = list(str(sys.argv[1]).replace('.','').replace(':','').replace('-',''))
cleanmac = mac2.copy()
l = [[":","-","-",".","."],[2, 5, 8, 11, 14],[6],[4,9],[2, 5, 8, 11, 14],[4,9]]
for g in range(0,len(l)-1):     #Loops through every list
    m = g; g+=1                       #while g steps through each list it also steps through each character
    for i in range(0,len(l[g])):       #looks up and loops the amount of character in the list 
        mac2.insert(l[g][i], l[0][m])  #inserts all the character in the list and in the the position of the lists.
    print("".join(mac2))     
    mac2 = cleanmac.copy()   # Clears for new characters
print("".join(mac2))     #Makes a list looks shiny 
