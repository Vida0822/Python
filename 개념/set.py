data = set([1,1,2,3,4,4,5])
print(data) # {1, 2, 3, 4, 5}

data = {1, 1, 2, 3, 4, 4, 5}
print(data) # {1, 2, 3, 4, 5}

a = set([1,2,3,4,5])
b = {3, 4, 5, 6, 7}
print(a|b) # {1, 2, 3, 4, 5, 6, 7}
print(a&b) # {3, 4, 5}
print(a-b) # {1, 2}

data = set([1,2,3])
print(data)

data.add(4)
print(data) # {1, 2, 3, 4}

data.update([5,6])
print(data) # {1, 2, 3, 4, 5, 6}

data.remove(3)
print(data) # {1, 2, 4, 5, 6}
