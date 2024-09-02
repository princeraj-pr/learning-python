# Removing duplicate items from the list without using set

some_list = ['a','b','c','b','d','m','n','n']
print(f"Original list: {some_list}")

position = 1
index = 0
for item in some_list:
  index = position
  while index < len(some_list):
    if str(item) == str(some_list[index]):
      some_list.pop(index)
    index += 1 
  position += 1
 
print(f"Final list: {some_list}")
