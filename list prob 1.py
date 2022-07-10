input_string = input('Enter elements: ')
list1 = input_string.split()
for i in range(len(list1)):
    list1[i] = int(list1[i])
temp= list1[0]
list1[0]=list1[len(list1)-1]
list1[len(list1)-1]=temp
print(list1)