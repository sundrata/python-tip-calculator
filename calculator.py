#Asks user how much their meal cost before tip/tax
amount = raw_input("What's your total before tip/tax?")

#Asks users the amount of sales tax applied to their meal
tax = raw_input("What is the sales tax applied to your meal? (Enter as whole number)")

#Asks user what percent gratuity they would like to apply
tip = raw_input("What percent tip would you like to apply? (Enter as whole number)")

#total is the amount with tax and tip included. We need to change every input into an integer to apply arithmetic. We also need to multiply the tax and tip by 0.01 because users input 
#these values as whole numbers rather than percentages.git 
total = int(amount) + (int(amount) * (int(tax) *.01)) + (int(amount) * (int(tip) * .01))

result = "Your suggested total is " + str(total)

print result 

