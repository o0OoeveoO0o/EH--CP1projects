# Eh Period 1 Shopping List Manager

shopp_lst = []

while True:
    act = input("What would you like to do? (add, remove, view, exit): ")
    
    if act == "add":
        itm = input("What item would you like to add? ")
        shopp_lst.append(itm)
        print("Your list:", " ".join(shopp_lst))
    
    elif act == "remove":
        itm = input("What item would you like to remove? ")
        shopp_lst.remove(itm)
        print("Your list:", " ".join(shopp_lst))
    
    elif act == "view":
        print("Your list:", " ".join(shopp_lst))
    
    elif act == "exit":
        print("Goodbye!")
        break
