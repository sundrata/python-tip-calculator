#Asks user how much their meal cost before tip/tax, converts string input to integer so arithmetic may be applied. 
amount = int(raw_input("What's your total before tip/tax?"))

#Asks users the amount of sales tax applied to their meal, converts string input to integer so arithmetic may be applied. Multiplies value by .01 because user enters whole number rather than percentage. 
tax = int(raw_input("What is the sales tax applied to your meal? (Enter as whole number)")) * .01

#Asks user what percent gratuity they would like to apply, converts string input to integer so arithmetic may be applied. Multiplies value by .01 because user enters whole number rather than percentage.
tip = int(raw_input("What percent tip would you like to apply? (Enter as whole number)")) * .01

#Arithmetic calculating the tax and tip amounts, then finds sum of original amount + tax + tip
total = amount + (amount * tax ) + (amount * tip )

result = "Your suggested total is $" + str(total)

print result 

