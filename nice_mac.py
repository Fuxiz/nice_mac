import sys
mac2 = str(sys.argv[1]).replace('.','').replace(':','').replace('-','')
macindex = [str(char) for char in mac2] 
cleanmac = macindex.copy()
l = [[":","-","-",".","."],[2, 5, 8, 11, 14],[6],[4,9],[2, 5, 8, 11, 14],[4,9]]
for g in range(0,len(l)-1):     #Loops through every list
    m = g
    g = g+1                     # Jumps to second list for the positions
    for i in range(0,len(l[g])):       #looks up and loops the amount of character in the list 
        macindex.insert(l[g][i], l[0][m])  #inserts all the character in the list and in the the position of the lists.
    print("".join(macindex))     
    macindex = cleanmac.copy()   # Clears for new characters
print("".join(macindex))     #Makes a list looks shiny 
