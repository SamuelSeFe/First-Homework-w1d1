my_name = "Samuel"
my_surname = "Serrano Ferraro"
my_full_name = my_name + " " + my_surname

my_age = 27
young = 35

while my_age <= young:
    print("My name is " + my_full_name + " and my age is " + str(my_age) + ".")
    print("I am still young.")
    my_age = my_age + 1

if my_age > young:
    print("My name is " + my_full_name + " and my age is " + str(my_age) + ".")
    print("I am now no longer young and my back hurts. :-(")
    