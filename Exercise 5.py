sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]

temp = sample_list.copy()
final_list = [] 

for num in sample_list:
    while num in temp: 
        temp.remove(num)
        if num in temp: 
            final_list.append(num)

print(final_list)

#Website's solution 1

import collections

duplicates = [] 

for item, count in collections.Counter(sample_list). items():
    if count > 1: 
        duplicates.append(items)

print(duplicates)

#Website's solution 2 

exist = {} 
duplicates = [] 

for x in sample_list:
    if x not in exist:
        exist[x] = 1 
    else: 
        duplicates.append(x)
    
print(duplicates)
