"""
Sum square difference

Answer: 25164150
"""
n = 100
vals = [*range(1,n+1)]
ans = []

for x in vals:
    # yay lambda function
    def squares(x): return x**2 
    ans.append(squares(x))
    
# sum of squares
sum_squares = sum(ans)
# square of sum of first n natural numbers
square_of_sum = sum(vals)**2
# Calculate the difference
diff = square_of_sum - sum_squares

print(f'{diff}')
