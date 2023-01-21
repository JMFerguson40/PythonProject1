
# Lists in Python are defined using square brackets []. For example:

my_list = [1, 2, 3, 4, 5]

# Common methods for lists include:
# append(x): adds an item to the end of the list
# extend(iterable): adds all items from an iterable (e.g. list, tuple) to the end of the list
# insert(i, x): inserts an item at a given position
# remove(x): removes the first item from the list that has a value of x
# pop(i): removes and returns the item at a given position (if no position is specified, the last item is removed and returned)
# index(x): returns the first index at which a given item appears in the list
# count(x): returns the number of times an item appears in the list
# sort(): sorts the items of the list in ascending order
# reverse(): reverses the order of the items in the list
# Dictionaries in Python are defined using curly brackets {}. The keys and values are separated by a colon. For example:

my_dict = {"apple": 1, "banana": 2, "cherry": 3}
# Common methods for dictionaries include:
#
# items(): returns a view object that contains the key-value pairs of the dictionary
# keys(): returns a view object that contains the keys of the dictionary
# values(): returns a view object that contains the values of the dictionary
# get(key): returns the value of the key, or None if the key is not in the dictionary
# pop(key): removes the key and its value from the dictionary and returns the value
# popitem(): removes and returns an arbitrary (key, value) pair from the dictionary
# update(other_dict): adds key-value pairs from another dictionary to the current dictionary
# Sets in Python are defined using curly brackets {}. For example:

my_set = {1, 2, 3, 4, 5}
# Common methods for sets include:
#
# add(x): adds an item to the set
# update(iterable): Update the set with the union of itself and others
# remove(x): removes an item from the set
# discard(x): removes an item from the set if it is present
# pop(): removes and returns an arbitrary item from the set
# clear(): removes all items from the set
# union(iterable): returns a new set containing all items from the set and all items from an iterable
# intersection(iterable): returns a new set containing items that are present in both the set and an iterable
# difference(iterable): returns a new set containing items that are present in the set and not in an iterable
# issubset(iterable): returns True if all items of the set are present in an iterable
# issuperset(iterable): returns True if all items of an iterable are present in the set

# Arrays in Python are not a built-in data type, but they can be created using the "array" module. For example:

import array
my_array = array.array('i', [1, 2, 3, 4, 5])
# Common methods for array include:

# append(x): Add an item to the end of the array
# extend(iterable): Extend the array by appending all the items from the iterable
# insert(i, x): Insert an item at a given position
# remove(x): Remove the first item from the array whose value is x
# pop(i): Remove and return the item at the given position in the array
# index(x): Return the index of the first item in the array whose value is x
# count(x): Return the number of times x appears in the array
# buffer_info(): Return a tuple (address, length) giving the current memory address and the length in items of the buffer used to hold array’s contents
# byteswap(): Reverse all the bytes of the items of the array.

