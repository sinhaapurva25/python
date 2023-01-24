def delete_multiple_element(list_object, indices):
    indices = sorted(indices, reverse=True)
    for idx in indices:
        if idx < len(list_object):
            list_object.pop(idx)
list_of_num = [[0,51], [0,52], [0,53], [0,54], [0,55], [0,56], [0,57], [0,58], [0,59]]
list_of_indices = [1, 0, 4, 2, 6]
# Remove elements from list_of_num at index 4,2 and 6
delete_multiple_element(list_of_num, list_of_indices)
print(list_of_num)