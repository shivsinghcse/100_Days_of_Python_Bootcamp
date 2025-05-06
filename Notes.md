# Day-01

## Output in python

- To print something in Python we use the `print()` function.
    ```python
    print("Hello World!")
    ```
- Strings are strings of characters.  
- For the new line we use `\n`.
  ```python
   print("Hi, I am Shiv Singh\nI am learning Python.")
  ```
-  String Concatenation is done with the + sign
  ```python
  print("Hello" + " " + "Shiv")
  ```
- Add spaces in code carefully.

## Type of errors
- Syntax Error
- Indentation Error
- Name Error
- Type Error
- Value Error


## Input in python
- To take input in python we use `input()` function. And write prompt for the user inside input function.
- It always returns string(str)
  ```python
   input("What is your name?")
  ```
## Comment
- In python, we write comment using `#`. Shortcut `ctrl + /`
- Comment are ignored by compiler.
```python
# this is a comment
```

## Variables in python
- To store data in the program we use variables.
```python
  x = 12
  name = input("What is your name?")
```
- You can use _ (underscore) for multiple words but, you can not use space.
- Variable name can not start with number.
- Keyword can not be used as variable name.
- To find the length of the string we use `len()` function.
  ```python
   name = "Ashutosh"
   print(name)
   print(len(name))
  ```
  
# Day-02
## Subscripting
- Accessing character of string
- Negative indexing is also allowed -1 refers last index.
  ```python
   print("Hello"[0])
   print("Hello"[-1])
  ``` 
## Data Types
- String = "Hello"
- Integer = whole number (12, -12, 0)
- Large Integer
  - print(123,456,789)
  - print(123_456_789) # ignores _ by compiler
- Float = Floating Point Number (1.2, -1.5)
- Boolean = (True / False)

## Type Error : 


## Type checking
- to check the data type we use the `type()` function
  ```python
    print(type(123)) # <class 'int'>
    print(type(1.23)) # <class 'float'>
    print(type("abc")) # <class 'str'>
    print(type(True)) # <class 'bool'>
  ```
  
## Type Casting
- converting one type of data to another type.
  ```python
    print(int("123") + int("2")) # 125
    int()
    float()
    str()
    bool()
  ```
- We can only concatenate str  (not "int") to str
  ```python
    print("123" + 4) # TypeError: can only concatenate str (not "int") to str
    print("123" + str(4)) # 1234
  ```
  
## Mathematical Operations
- Addition (+)
- Substraction (-)
- Multiplication (*)
- Division (/) : it always return float value, default behaviour of python
  ```python
   print(3 / 3) # 1.0
   print(type(3 / 3)) #<class 'float'>
  # to prevent this  we have // operator
  ```
- Division (//) : it return integer value
  ```python
    print(5 / 3) # 1.6666666666666667
    print(5 // 3) # 1
  ```
- Modulo (%) : it returns remainder
  ```python
   print(5 % 3) # 2
  ``` 
  
- Exponentation (**) : it returns the power
  ```python
   print(2**3) # 8
  ```

## PEMDAS / PEMDASLR :   
- Parentheses, Exponents, Multiplication/Division, Addition/Subtraction.
- If you have same order operator than we will solve it left to Right

  ```python
   print(3 * 3 + 3 / 3 - 3) # 7.0 
   print(3 * (3 + 3) / 3 - 3) # 3.0 
  ```

- BMI =  weight / (height * height)
- Flooring (int(3.123)) # 3  
- Round (round(3.623)) # 4  
- Round (round(3.123, 2)) # 3.12  

    ```python
     print(30.85399449035813)
     print(int(30.85399449035813)) # flooring the number = 30
     print(round(30.85399449035813)) # rounding = 31
     print(round(30.85399449035813, 2)) # rounding upto 2 digit after decimal
    ```
  
## Assignment operator:
- =
- +=
- -=
- *=
- /=


## S-string :
- write `f` before `""`
  ```python
    is_winning = True
    score = 1
    print("Your score is : " + str(score))
    # f-string
    print(f"Your score is = {score} and your winning status is {is_winning}")
  ```