#EH p1 Order UP 
coins = 9
Porkrind = {
    "Habilities":{
        'Spread': 4,
        'Chaser' : 4,
        'Roundabout' : 4,
        'Lobber' : 4, 
        'Charge' : 4,
        'Crackshot' : 4,
        'Converge' : 4,
        'twist up' : 4,

    },
    "Charms" : {
        'Heart' : 3,
        'Smoke Bomb' : 3,
        'P.Sugar' : 3,
        'Coffee' : 3,
        'Whetstone' : 3,
        'Twin heart' : 5,
        'Heart ring' :3,
        'Broken relic' :1,
    }

}
print("Coins = " , coins)
values = list(Porkrind.values())
keys = list(Porkrind.keys())

for key in keys:
    print(f"{key} are {Porkrind[key]}")

print("Welcome to Porkrind’s Emporium")
Porkrindlist = list(values,keys)
while True:
    buyMYSTUFF =input("Do you want to buy? ")

    if buyMYSTUFF == "yes":
        
        Porkrindlist.append