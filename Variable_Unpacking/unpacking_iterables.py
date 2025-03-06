1. Unpacking a Tuple
		t = (1, 2, 3)
		a, b, c = t
		#a,b,c = (1, 2, 3)
		print(a, b, c)  # Output: 1 2 3


2. Unpacking a List
		l = [10, 20, 30]
		x, y, z = l
		#x, y, z = [10, 20, 30]
		print(x, y, z)  # Output: 10 20 30

3. Unpacking a set
		s = {10, 20, 30}
		x, y, z = s
		#x, y, z = {10, 20, 30}
		print(x, y, z)  # Output: 10 20 30
		
4. Using * for Variable-Length Unpacking for lists.
***The * operator allows capturing multiple elements into a list.*****
		
		numbers = [1, 2, 3, 4, 5]
		first, *middle, last = numbers
		print(first)   # Output: 1
		print(middle)  # Output: [2, 3, 4]
		print(last)    # Output: 5
		
5. Using * for Variable-Length Unpacking for Tuples.

		numbers = (1, 2, 3, 1, 4, 5,1,2,6)
		first, *middle, last = numbers
		print(first)   
		print(middle)  
		print(last) 
		
Output:- 
1
[2, 3, 1, 4, 5, 1, 2]
6



6.  Using * for Variable-Length Unpacking for sets.

		numbers = {1, 2, 3, 1, 4, 5,1,2}
		first, *middle, last = numbers
		print(first)   
		print(middle)  
		print(last)    
		
Output:-

1
[2, 3, 4]
5
