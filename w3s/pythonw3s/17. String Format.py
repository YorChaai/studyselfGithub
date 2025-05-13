age = 36
txt = "My name is John, I am " + age
print(txt) #error must be str, not int

#But we can combine strings and numbers by using f-strings or the format() method!

age = 46
txt = f"My name is Diofavian, i am {age}"

print(txt)

#A placeholder can contain variables, operations, functions, and modifiers to format the value.

price = 69
txt = f"The price of nasi is {price} dolar"

print(txt)

price = 69
txt = f"The price of nasi is {price:2f} dolar"

print(txt) #69.000000

price = 69
txt = f"The price of nasi is {price:.2f} dolar"

print(txt) #69.00


txt = f"The price of nasi is {20 * 3} dolar"

print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)



