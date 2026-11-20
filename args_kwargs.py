def hello(name,*args):
    print(args)
    for first in args:
        print(f"Hello {first} {name}!!")
hello("triple t", "Tralalero", "Chocolatini peruanini","Orcalero orcala")
hello("Zeta","MI BOMBO")


def clean(decimals=0,**kwargs):
    if not kwargs.get("type"):
        return"I AM SO TIRED FAAAh"
    if kwargs.get("type") == "str":
        return kwargs.get("type").strip().lower()
    elif kwargs.get("type") == "int":
        return int(kwargs)["type"]
    elif kwargs.get("type") =="Float":
         if kwargs.get("decimals"):
             decimals = kwargs.get("decimals")
         return round(float(kwargs.get("type")),kwargs["Descimals"])
    elif kwargs.get("type") == "list":
        return str(f"{x}," for x in kwargs.get("type"))
    elif kwargs.get("type") == "bool":
        return f"{kwargs.get("type")}"
   
print(clean(type = "float", data="3.1415", decimals = 3))
print(clean(data= "utah" , type= "str"))
print()
