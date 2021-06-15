d1 = {
    'A' : 65, 
    'B' : 66, 
    'C' : 67, 
    'D' : 68,
    'E' : 69, 
    'F' : 70,
    }

l1 = ['A', 'C', 'F']
temp = [] 
for item in d1:
    if item not in l1:
        temp.append(item)  

for i in temp:
    d1.pop(i)

print(d1)

#Websites solution 

new_dict = {key: d1[key] for key in l1}

print(new_dict)
