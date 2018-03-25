
name = input("What is your name? ")

# If length of name is greater than 20,
# print something

if len(name) > 20:
    print("Your name is too long, type a shorter name.")


age = int(input("What is your age? "))

# If age is less than 10, print "Smol"
# ELse if age is between 10 and 20, print "Big boi"
# Else, print "Big big boi"

if age < 10:
    print("Smol")
elif age > 10 and age < 20:
    print("Big boi")
else:
    print("Big big boi")

coolness = float(input("Rate your coolness out of 100.0 = "))

# If coolness is more than 100.0, just print some error

if coolness > 100.0:
    print("Not possible!")
elif coolness > 75.0:
	cool_index = "Hella Rad",
elif coolness > 50.0:
	cool_index = "Pretty Nice"
elif coolness > 25.0:
	cool_index = "Kinda Sick"
else:
    cool_index = "Pretty Sad"

# Now print a string like
# My name is Arnold Tan, I am 69 and I'm Really Cool

print("My name is " + name + ", I am " + str(age) + " and I'm " + cool_index)
