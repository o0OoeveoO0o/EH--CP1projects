# Ravager Snack Bar
import random
pirate_name = input("What's your name, pirate? ")
snack_name = input("What snack do you want? ")
price = random.randint(2, 8)  # random price in credits
#1 transform the variable below by adding an INT
quantity = int(input("How many would you like? "))
total = price * quantity
#2 the old one was total - 2 * 0.10 but  it was just subtracts 2 now we have a 10% discount
discounted_total = total - total * 0.10
tax_rate = 0.08
total_with_tax = discounted_total + (discounted_total * tax_rate)
print("Hello, " + pirate_name + "! Here's your order summary:")
print("Snack: " + snack_name) #3 <- Name error
print("Price per snack: " + str(price) + " credits")
#4 now it prints the real correct variable
print("Total before tax: " + str(discounted_total))
print("Total with tax: " + str(round(total_with_tax, 2)) + " credits")# 5<- missing parentesis
