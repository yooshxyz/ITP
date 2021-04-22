list1 = [1, 2, 3, 4, 5]
list2 = [0, 1, 2, 3, 4]
sum_list = []
x = 0
while x != 5:
  for i in range(0, 5):
    sum_list.append(list1[x] + list2[i])
  x += 1
print(sum_list)
print(sum_list.sort())