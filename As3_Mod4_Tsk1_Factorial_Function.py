# Defines a function named factorial that takes a number as an argument
# and calculates its factorial using a loop and recursion.
# Returns the calculated factorial.


# Factorial function using FOR loop
def fact_for(a):
    f=1
    for n in range(1,a+1):
        f = f * n
    return f

# Factorial function using RECURSION
def fact_rec(x):
    if x==0:
        return 1
    else:
        return x * fact_rec(x - 1)

num=int(input("Enter a number: "))

res_fact_for = fact_for(num)
res_fact_rec = fact_rec(num)

print(f"Factorial of {num} calculated using FOR loop is:", res_fact_for)

print(f"Factorial of {num} calculated using RECURSION is:", res_fact_rec)

