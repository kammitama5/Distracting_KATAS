Recursion with Memoization

Recursion is not always good

Typical Fib(n):
 if n <= 1
   return n
 else
   return Fib(n-1)+Fib(n-2)
   
Recursion Tree -> duplicates -> increases time and space of prog
Avoid recalculation of space -> save memory

Fib(n)
base condition:
if n <= 1
	return n 
if Fn is in memory
    return Fn 
else
    Fn -> Fib(n-1) + Fib(n-2)
	save Fn in memory
	return Fn
