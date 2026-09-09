#Evans Hidalgo p1 idiot proof
firsat_name = input("Please insert your first name: ").strip().title()
las_name = input("Now insert your last name:  ").strip().title()
#asks first and last name WOoOoAah!!
first_sep =firsat_name.split()
fixed="".join(first_sep)
lst_sep = las_name.split()
last_fixed = "".join(lst_sep)
#fixes the errors a user can make
full_nam = fixed.title() + " " +last_fixed.title()
#connects everything
print("Your name is: " + full_nam)



while True :
    try :
        phone_N = input("that\'s not a number please insert a real one: "). strip()
        if len(phone_N) !=10 or not phone_N.isdigit():
           raise ValueError
      
        return phone_N
      
    except ValueError:
        print("Your phone number is " + phone_N)

