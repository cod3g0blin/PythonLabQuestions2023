#Write a program to compute compound interest using keyword arguments
def compute_CI(principal, rate, time):
    compound_interest = principal * (1 + rate) ** time - principal
    return compound_interest

p = float(input("Enter the principal amount: "))
r = float(input("Enter the interest rate (in decimal form): "))
t = int(input("Enter the time period (in years): "))

interest = compute_CI(principal=p, rate=r, time=t)

print("Compound Interest:", interest)
