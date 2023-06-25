def selection_sort(values):
    sorted_lst = []
    for i in values:
        index_to_move = index_of_min(values)
        print(index_to_move,values[index_to_move],sorted_lst)
        small = values.pop(index_to_move)
        sorted_lst.append(small)
    return sorted_lst
def index_of_min(values):
    min = values[0]
    for i in values:
        if i < min:
            min = i
    return values.index(min)

print(index_of_min([62,6,12,616,1222,0]))
print(selection_sort([[62,6,12,616,1222,0]]))