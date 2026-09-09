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
    phone_N = input("What is your phone number? "). strip()
    try :

        if len(phone_N) !=10 or not phone_N.isdigit():
           raise ValueError
        
    except ValueError:
        print("That's not a valid phone number")

    else:
        break



print("Your number is " + phone_N[:3]  + " " + phone_N[3:6] + " " + phone_N[6:])


while True :
 try :
     gpa = float(input("What is your gpa? "))
 except ValueError:
     print("That's not a valid gpa")

 else:
     break
 

print("Your gpa is " , round(gpa,1))
#finished
