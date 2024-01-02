List = [1, 5, 2, 9, 3, 22, 13]

def listSortingFun(list):
   for i in range(len(list)):
       for j in range(len(list) - i - 1):
           if list[j] > list[j+1]:
               list[j], list[j+1] = list[j+1], list[j]
  
   return list

sorted_list = listSortingFun(List)
print(f"Sorted list in ascending order: {sorted_list}")
