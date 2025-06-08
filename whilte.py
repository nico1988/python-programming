# while demo
i = 0
while i < 5:
    print(i)
    i += 1 
# another example
print("while loop with break")
i = 0
while True:
    if i >= 5:
        break
    print(i)
    i += 1
# another example with continue
print("while loop with continue")
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)