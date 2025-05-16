print(9 >= 10)
print(9 == 9)
print(9 <=9 )


a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

print(bool("Hello"))
print(bool(""))
print(bool("0"))


x = "Hello"
y = 15

print(bool(x))
print(bool(y))

print(bool("Hello"))
print(bool(""))
print(bool("0"))
print(bool(["Hello", "World", "Dio"]))


print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))


class myclass:
  def __len__(self):
    return 0

obj = myclass()
print(bool(obj))


def myFunction() :
  return True

print(myFunction())


def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")


def myFunction():
  return True

print(myFunction())






