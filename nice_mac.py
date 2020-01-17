import sys
mac = str(sys.argv[1])
mac = mac.replace('.','').replace(':','').replace('-','')
charmac = [] 
for char in mac:
    charmac.append(str(char)) 
macindex = charmac.copy()
l = [[":","-","."],[2, 5, 8, 11, 14],[4,9],[2, 5, 8, 11, 14]]
for g in range(0,len(l)-1):     #Loops through every list
    m = g
    g = g+1                     # Jumps to third list to use the amount of space
    for i in range(0,len(l[g])):       #looks up and loops the amount of character in the list 
        charmac.insert(l[g][i], l[0][m])  #inserts all the character in the list and in the the position of the lists. With power of 0 i always stay at the characters
    print("".join(charmac))     
    charmac = macindex.copy()   # Clears for new characters
print("".join(charmac))     #Makes a list looks shiny 
macindex.insert(6,"-")
print("".join(macindex))
