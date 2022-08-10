import itertools

print(itertools.combinations("ABC",2)) # <itertools.combinations at 0x1916522f130>

print(list(itertools.combinations("ABC",2))) # [('A', 'B'), ('A', 'C'), ('B', 'C')]

print(list(itertools.combinations("AABC",2)))
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('A', 'B'), ('A', 'C'), ('B', 'C')]

print(list(itertools.combinations("ABCD",3)))
# [('A', 'B', 'C'), ('A', 'B', 'D'), ('A', 'C', 'D'), ('B', 'C', 'D')]