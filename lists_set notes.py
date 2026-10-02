
#lists
siblingsofmyteacher = ["Alex", "Katie" , "Andrew" , "Tia","Treyson", "Xavier","Jake"]   #If you don't save your variables are not going to work| to make a list we use brackets "[]" around them | commas "," for separating and each item must be a proper data type
lenght = len(siblingsofmyteacher)
#complex data type hold many peaces of information 
#every item have a number "Alex" = 0 "Katie" = 1 "Andrew" = 2
print(f"My older sister is {siblingsofmyteacher[1]}")
print(*siblingsofmyteacher) #<- the "*" helps to not put the  [] while it is printing NAME IS UNPACKING OPERATOR?
print(f"The youngest is {siblingsofmyteacher[-1]}")
siblingsofmyteacher.append("Jashree") #adds somethings to the list
print(*siblingsofmyteacher)
siblingsofmyteacher.insert(3,"Vienna")#insert  a name in the space that you want
print(*siblingsofmyteacher)
siblingsofmyteacher.extend(["Joe" , "Israel", "Zee"])
print(*siblingsofmyteacher)
siblingsofmyteacher.remove("Vienna") #<-deletes a item from the list
print(*siblingsofmyteacher)
siblingsofmyteacher.pop(0) #removes the item you put if in the numbre you put and if you do not put any number deletes the last item
print(*siblingsofmyteacher)
#************************************
#Tuples
subjects = ("CP1","CP2" , "Advanced CP" , "CSP" , "Utah studies" , "US 1","US 2" , "World civ", "World Geography" , "CCA business")
print(subjects[0])
print(*subjects)
#Lists	[]	      	ordered	 		mutable   |Duplicates
#Tuples	()		ordered			    immutable |Duplicates
#Set    {}      unordered           mutable   |No duplicates
#set(variable name)
#Sets
visited = {"Texas" , "Ohio","Minnesota", "Virginia", "D.C", "Utah","California", "Nevada"}

print(*visited)
print(len(visited))
visited.add ("Idaho")
print(*visited)
visited.update({"Montana", "Arizona" , "Oklahoma" , "New Mexico"})
print(*visited)
visited.remove("Arizona")
print(*visited)


#                       00                  00
#                    00     00          00      00
#                 00            00   00            00
#                00                00               00
#               00                 00       0       00
#               00         0       00      000      00
#                00       000     0  0      0       00
#                 o00      0    00   00           00
#                o   00        00     00         00
#               o       00     00       00       0
#              o          00               000
#             o
#
#
#
#
#
#
#
#
#
#
#
#
#
