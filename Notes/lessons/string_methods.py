"""#Evans Hidalgo p1 Programming notes

sentence = "The quick brown fox jumps over the lazy dog"

fixed = sentence.replace("fox",'wolf')

name = input("What is your name ").strip().title()
word = input("What word do you want? ").strip().lower()
word2 = input("New word: ").strip().lower()
ocation = sentence.find(word)
newsentece = sentence.replace(word,word2)
print("Hello " +name)

print(sentence.find("over"))

print(sentence.split('the'))


print(sentence.lower())
print(sentence.upper())
print(sentence.capitalize())
print(sentence.title()) #
print(fixed)
print(newsentece)
print(sentence.split())

firsat_name = input("What is your first name? ").strip().title()
last_name=input("What is your last name? ").strip().title()
first_separated =firsat_name.split()
fixed="".join(first_separated)
last_separated= last_name.split()
last_fixed = "".join(last_separated)
full_name = fixed.title() + " " +last_fixed.title()
print("Hello " + full_name.title())

print(full_name.isalpha())#chacks if the entire thing are letters
print(full_name.isnumeric())#checks if the entire thing is numbersnumeric
print(full_name.isupper())#checks if the entire thing is upper
#formtating string
print(f"Hello {fixed.title()} {last_fixed}welcome to my program!")""" #<- Multiline comment
letter = input("give me a letter: ")
letter = letter [0].lower()
number_value = ord(letter) #ord = looking at the numeric value of each character
number_value += 2
new_letter = chr(number_value)#convert a number into a letter
print(f'Your letter was {letter} now it is {new_letter}')