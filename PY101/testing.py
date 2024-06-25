x = ['a', 'b', 'c', 'd']

def mutate_list_o_strings(list_of_strings):
    new_lst = []
    for i in list_of_strings:
        i = i.upper()
        new_lst.append(i)
    
    return new_lst
    

print(mutate_list_o_strings(x))
print(x)