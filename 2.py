"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

When n = 33: ...  
    - The fib list: [2, 8, 34, 144, 610, 2584, 10946, 46368, 196418, 832040, 3524578] 
      * We stop since the next fibonacci number would exceed 4 million.
    - The fib(33): 4613732
"""

def fib(n):
    """This is a recursive function
    to find the fibonnacci of an integer"""
        
    if n < 2:
        return 1
    else:
        return (fib(n-1) + fib(n-2))

from itertools import takewhile
num = 33
even_sum = 0

even_list = (list(takewhile(lambda x: x <= 4000000, [f for i in range(num) if (f :=fib(i))%2 ==0])))
even_sum = sum(even_list)
print("The fib list:", even_list)
print("The fib(%d): %d" % (num, even_sum))
