thislist = ["nami", "namu", "duni"]
thislist.remove("namu")

print(thislist)

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.pop(0)

print(thislist)


thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.pop(0)
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[1]
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist
print(thislist) #error because thislist dont have variabel

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)