#List_Programs


newlist = ["sample" , "sample1" , "sample2" , "sample3"] 
#Printing list, Lists are used to store multiple items in a single variable.
print(newlist)


print(len(newlist)) #List Length, To determine how many items a list has, use the len() function
lists = ["1234", "AJay", "true" "male"]
 #List Items - Data Types
print(lists)
list2 = list(("Buggy", "Dacia", "Maclaren", "Tesla", "UAZ","Boat"))
 #The list() Constructor, note the double round-brackets.

print(type(list2))
print(list2[4]) 
#Access Items, List items are indexed and you can access them by referring to the index number.

print(list2[-6]) 

#Negative indexing

print(list2[2:5]) 

#Range of Indexes
print(list2[:4])
print(list2[2:])



list3= list(("Buggy", "Dacia", "Maclaren", "Tesla", "UAZ","Boat")) 

#Change Item Value,replacing the fourth itemChange the second item.

list3[3] = "tripla"

list3 [1:3] = ["car" , "Train"]

print(list3)

list4= list(("Buggy", "Dacia", "Maclaren", "Tesla", "UAZ","Boat")) #inserting items

list4.insert(5,"Thar")

print(list4)

#Insert Items,To insert a new list item, without replacing any of the existing values.

list5= list(("Chandigarh", "Panchkula", "Derabassi", "Ramgarh")) #adding items to end. using append()

list5.append("Pinjore")

print(list5)

list5.remove("Derabassi") 
#removing specific item from list

print(list5)


list5.pop(3) 
#removing specified index from list using pop().

print(list5)

list6= list(("Chandigarh", "Panchkula", "Derabassi", "Ramgarh")) #deleting specific index from list

del list6[0]

print(list6)

list4.clear() 
#clearing whole list4 content but list still remains.

print(list4)

list7 = list(("tadaaa", "tararumpum", "pumtum"))
list8 = list(("combing", "both" ,"list7&list8"))
list9 = list7 + list8
print(list9)
#adding both list 