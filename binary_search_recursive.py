def binary_search(a_list, item):
    print(a_list)
    if len(a_list) == 0:
        return Fale
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            return Ture
        else:
            if item < a_list[midpoint]:
                return binary_search(a_list[:midpoint], item)
            else:
                return binary_search(a_list[midpoint + 1], item)

test_list=[0,1,2,8,13,17,19,32,42,]
print(binary_search(test_list, 3))
print(binary_search(test_list, 13))
      
        
    
