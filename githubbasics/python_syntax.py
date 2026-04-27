#
from os.path import sep

print("Hello world")

name = "Michael"
print(name)

age = 20

if age >= 18:
    print("You´re old enough")
else:
    print("You´re too young")

first_num, second_num, third_num = 12, 23, 45

print(second_num)

DATE_OF_BIRTH = "19/12/2020"
print(DATE_OF_BIRTH)

message = "Collect my keys from the driver"
print(message)

message = "Tell collier i will deduct 15% "
print(message)

price_of_product = 34
student_name = "Michael"
price_of_yam = 23.56
is_married = False

one_line_sentence = ("I love programming,"
                     "It pays me nothing."
                     "Programming changed my life,"
                     "It is sometimes boring.")
print(one_line_sentence)

poem = """           I love programming,
                     It pays me nothing.
                     Programming changed my life,
                     It is sometimes boring. """

print(poem)

person_age = 17
is_adult_person = person_age >= 18
print(person_age)

try:
    any_num = int("456")
    print(any_num)
except ValueError:
    print("Invalid input. not a number")

print("Programming ", "Python ", "Awsome", sep="---")

