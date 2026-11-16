#EH 1st p combat game
import random

def get_user_stats():
    print("You received a letter inviting you back to the old studio where you used to work 30 years ago to commemorate the old times.")
    print("Letter: Dear Henry,")
    print("It seems like a lifetime since we worked on cartoons together. 30 years really slips away, doesn't it?")
    print("If you're back in town, come visit the old workshop. There's something I need to show you.")
    print("Your best pal,")
    print("Joey Drew\n")
    
    print("Who are you?")
    print("1. Henry (Buddy)")
    print("2. Boris")
    print("3. Allison Pendle")
    choosepls = int(input())
    
    if choosepls == 1:  # Henry
        stats = {"name": "Henry", "health": 35, "defense": 16, "atk": 4, "dmg": 5}
    elif choosepls == 2:  # Boris
        stats = {"name": "Boris", "health": 40, "defense": 14, "atk": 3, "dmg": 6}
    else:  # Allison Pendle
        stats = {"name": "Allison Pendle", "health": 28, "defense": 12, "atk": 5, "dmg": 7}
    
    print(f"\nHealth: {stats['health']}  Defense: {stats['defense']}")
    print(f"Attack: D20 + {stats['atk']}  Damage: D8 + {stats['dmg']}")
    return stats


def user_turn(player, monster):
    print("\nWhat would you like to do?")
    print("1. Normal Attack")
    print("2. Wild Attack (double damage, but you take damage)")
    print("3. Heal (+9 HP)")
    print("4. Flee")
    
    choice = int(input())
    
    if choice == 1:
        roll = random.randint(1, 20) + player["atk"]
        if roll > monster["defense"]:
            dmg = random.randint(1, 8) + player["dmg"]
            monster["health"] -= dmg
            print(f"You hit! Bendy takes {dmg} damage. HP left: {max(0, monster['health'])}")
        else:
            print("You miss!")
    
    elif choice == 2:
        roll = random.randint(1, 20) + player["atk"]
        if roll > monster["defense"]:
            dmg = (random.randint(1, 8) + player["dmg"]) * 2
            monster["health"] -= dmg
            self_dmg = random.randint(2, 5)
            player["health"] -= self_dmg
            print(f"Wild hit! {dmg} damage to Bendy, but you take {self_dmg}.")
            print(f"Bendy HP: {max(0, monster['health'])} | Your HP: {max(0, player['health'])}")
        else:
            print("Wild attack misses!")
    
    elif choice == 3:
        player["health"] += 9
        print(f"You heal 9 HP. Now at {player['health']}")
    
    elif choice == 4:
        if random.randint(1, 100) <= 40:
            print("You escaped!")
            return "fled"
        else:
            print("You failed to flee!")
    
    return "continue"


def monster_turn(player, monster):
    print("\nBendy attacks!")
    roll = random.randint(1, 20) + 4
    if roll > player["defense"]:
        dmg = random.randint(1, 8) + 4
        player["health"] -= dmg
        print(f"Bendy hits you for {dmg}! Your HP: {max(0, player['health'])}")
    else:
        print("You block the attack!")


def combat():
    player = get_user_stats()
    
    monster = {"name": "Bendy", "health": 40, "defense": 14}
    
    print(f"\nYou are attacked by Bendy the Ink Demon!")
    
    turn = "player" if random.randint(1, 2) == 1 else "monster"
    print("You move first!" if turn == "player" else "Bendy moves first!")
    
    while player["health"] > 0 and monster["health"] > 0:
        if turn == "player":
            result = user_turn(player, monster)
            if result == "fled":
                return
            turn = "monster"
        else:
            monster_turn(player, monster)
            turn = "player"
    
    print("\n" + "="*40)
    if player["health"] <= 0:
        print("Bendy wins... You are lost in the ink.")
    else:
        print(f"You defeated Bendy! Congratulations {player['name']}!")
    print("="*40)


if __name__ == "__main__":
    combat()
