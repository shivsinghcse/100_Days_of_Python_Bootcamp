# print(len("Shiv"))
#  print(len(1234))  # TypeError: object of type 'int' has no len()

# Subscripting
# print("Hello"[0])
# print("Hello"[4])
# print("Hello"[-1])
# print("Hello"[-5])

# String
# print("123" + "345")

# Integer = whole number

# print(123+456)

# Large Integers
# print(123,456,789)
# print(123_456_789) # ignores _ by compiler

# Float = Floating point number

# print(3.14)

# Boolean : True / False
# print(True)
# print(False)



# print(len('123'))

# print(type(123))
# print(type(1.23))
# print(type("abc"))
# print(type(True))

# Type casting
# print(int("123") + int("2"))
# print(int("abc"))

# print("123" + 4) # TypeError: can only concatenate str (not "int") to str
# print("123" + str(4))

# print("Number of letters in your name: " + str(len(input("Enter your name?\n"))))

# name_of_the_user = input("Enter your name?\n")
# length_of_the_name = len(name_of_the_user)
# print(type(name_of_the_user))
# print(type(length_of_the_name))
# print("Number of letters in your name: " + str(length_of_the_name))

# print(2 + 3)
# print(type(2 + 3))

# print(2 - 3)
# print(type(2 - 3))

# print(2 * 3)
# print(type(2 * 3))

# print(3 / 3)
# print(type(3 / 3))

# print(5 % 3)
# print(type(5 % 3))
#
# print(5 / 3)
# print(5 // 3)

# print(2**3)

# print(3 * 3 + 3 / 3 - 3) # 7.0
# print(3 * (3 + 3) / 3 - 3) # 3.0

weight = 84
height = 1.65

bmi = weight / height ** 2

# print(bmi)
# print(int(bmi)) # flooring the number
# print(round(bmi)) # rounding
# print(round(bmi, 2)) # rounding upto 2 digit after decimal

score = 0
height = 1.7
is_winning = True
score += 1
print(score)

# f-string
print("Your score is : " + str(score))
print(f"Your score is = {score} and your winning status is {is_winning}")
