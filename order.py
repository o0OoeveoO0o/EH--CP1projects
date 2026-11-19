#EH p1 Order UP 
coins = 9

Porkrind = {
    "Abilities": {
        'Spread': 4,
        'Chaser': 4,
        'Roundabout': 4,
        'Lobber': 4,
        'Charge': 4,
        'Crackshot': 4,
        'Converge': 4,
        'Twist Up': 4,
    },

    "Charms": {
        'Heart': 3,
        'Smoke Bomb': 3,
        'P. Sugar': 3,
        'Coffee': 3,
        'Whetstone': 3,
        'Twin Heart': 5,
        'Heart Ring': 3,
        'Broken Relic': 1,
    }
}

print("Coins =", coins)

for category in Porkrind:
    print(f"\n{category}:")
    for item, price in Porkrind[category].items():
        print(f"  {item} - {price} coins")

inventory = []

print("\nWelcome to Porkrind's Emporium!")

while True:
    buyMYSTUFF = input("\nDo you want to buy? (yes/no): ").lower()

    if buyMYSTUFF == "no":
        break

    elif buyMYSTUFF == "yes":
        item_name = input("Enter item name: ")

        found = False

        for category in Porkrind:
            if item_name in Porkrindprice = Porkrind[category][item_name]

                if coins >= price:
                    coins -= price
                    inventory.append(item_name)
                    print(f"You bought {item_name}!")
                    print(f"Coins left: {coins}")
                else:
                    print("Not enough coins!")
                found = True
                break

        if not found:
            print("Item not found.")

    else:
        print("Please enter yes or no.")

print("\nInventory:", inventory)
print("Coins remaining:", coins)
    buyMYSTUFF =input("Do you want to buy? ")

    if buyMYSTUFF == "yes":
        
        Porkrindlist.append
