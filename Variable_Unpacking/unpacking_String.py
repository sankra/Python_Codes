#This code shows how to unpack string.

a , b , c = '123'
b , c , d = '456'
print(a,b,c,d)

#output: 1 4 5 6

##or

t = '123'
s = '456'
a,b,c = t
b,c,d = s
print(a,b,c,d)

#output: 1 4 5 6
