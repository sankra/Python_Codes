mylist = [2, 4, 6, 8, 10, 12, 14, 16] 
mylist[1:5] = [] #performing indexing on the list.
print (mylist)

#output
#[2, 12, 14, 16]

#Here, at line no 4 we are assigning a empty list [] at mylist[1:5],thus the empty list is replacing 4,6,8,10 values in the mylist.
#Therefore the output is [2, 12, 14, 16]
