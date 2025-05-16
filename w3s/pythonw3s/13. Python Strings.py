print("hello")
print('hello')


print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')


a = "hello"
print(a)

a = """1Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''2Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)


a = "Hello, World!"
print(a[6]) # nothing


for x in "banana":
    print(x)

for x in ("orange"):
    print(x)

for x in ("banana", "papaya"):
    print(x)

a = "Hello, World"
print(len(a))


txt = "The best things in life are free!"
print("free" in txt)


txt = "The best things in life are free!"
if "best" in txt:
    print("yes, text in txt")

else:
    print("No, best not in txt")

txt = "The best things in life are free!"
print("best1" not in txt)

txt = "The best things in life are free!"
if "best1" not in txt:
    print("No, best1 not in txt")

else:
    print("Yes, best1 in txt")


