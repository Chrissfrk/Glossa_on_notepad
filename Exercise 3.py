#Exercise 3 
number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

def remove_items(number_list):
    i = 0 
    while i <= (len(number_list) - 1):
            if number_list[i] > 50: 
                number_list.pop(i)
                i = 0 
            i += 1
    print(number_list)

remove_items(number_list)