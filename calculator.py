#fixed tab ammount
amount = 10

# sales tax, fixed to 7%
tax = .07

# suggested tip percentage fixed to 15%
tip = 0.15

#total is the amount with tax and tip included
total = (amount + (amount * tax) + (amount * tip))

result = "Your suggested total is " + str(total)

print result