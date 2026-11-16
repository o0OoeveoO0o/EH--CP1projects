

car = {#Key : Value,
    "make" : "Jeep" ,
    "model": "Wranger",
    "color" : "silver",
    "year" : 2023
}

values = list(car.values())


print(values)
print(len(car))
if "transmission" in car:
    print(car["transmission"])
else:
    car["transmission"] = "automatic"

car.pop("color")
print(car.items())
keys = list(car.keys())

for key in keys:
    print(f"{key} is {car[key]}")



avatar = {
    "water":{
   "Katara" : "Water bender",
    "Sokka" :"Leader, Boomerang Guy, Idea Guy"
    },
    "Earth": {
        "Toph" : "Earth Bender",
        "Suki" : "Warrior from Kyoshi Island",
        "Cabbage Merchment" : "My CABBAGES!!!1!1!!"
    },
    "Air":{
        "Aang" : "Air bender, The Avatar"
    },
    "Fire":{
        "Zuko": "Fire bender future fire lord",
        "Iroh" : "Fire bender, Dragon of the west",
        "Azula" : "Fire lord for 1 hour fire bender"
    }
}

print(avatar["Fire"]["Iroh"])
print(avatar.get("Earth") .get("Bumi"))