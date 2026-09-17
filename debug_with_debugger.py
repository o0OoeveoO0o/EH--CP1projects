# Ravager Snack Bar
import random

pirate_name = input("What's your name, pirate? ")
snack_name = input("What snack do you want? ")

price = random.randint(2, 8)  # random price in credits
quantity = input("How many would you like? ")

total = price * quantity

discounted_total = total - 2 * 0.
                        #^ Wrong sign

tax_rate = 0.08
total_with_tax = discounted_total + (discounted_total * tax_rate)

print("Hello, " + pirate_name + "! Here's your order summary:", total_with_tax ) #<-- ADD THE TOTAL TO THE PRINT STATEMENT
print("Snack: " + snack_name) #<--Wrong name for the variable
print("Price per snack: " + str(price) + " credits")
print("Total before tax: " + str(price))
print("Total with tax: " + str(round(total_with_tax, 2)) + " credits") #<- missing parentesis