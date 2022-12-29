"""
   Once a tuple is created, we cannot change its values. 
   Tuples are unchangeable, or immutable as it also is called.
   But there is a workaround. We can convert the tuple into a list,
   change the list, and convert the list back into a tuple.
"""

x = ("apple", "banana", "cherry")
y = list(x)

#Change banana to kiwi
y[1] = "kiwi"
x = tuple(y)

print(x)