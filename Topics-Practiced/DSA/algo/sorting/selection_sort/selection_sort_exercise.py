def swap(dct, a, b):
    if a!=b:
        temp = dct[a]
        dct[a] = dct[b]
        dct[b] = temp


def selection_sort(dct: list, keys:list):
    for key in keys:
        for i in range(len(dct)-1):
            min_index = i
            for j in range(i):
                if ord(dct[j][key]) < ord(dct[min_index][key]):
                    min_index = j
                swap(dct, j, min_index)



if __name__ == "__main__":
    dct = [
            {'First Name': 'Raj', 'Last Name': 'Nayyar'},
            {'First Name': 'Suraj', 'Last Name': 'Sharma'},
            {'First Name': 'Karan', 'Last Name': 'Kumar'},
            {'First Name': 'Jade', 'Last Name': 'Canary'},
            {'First Name': 'Raj', 'Last Name': 'Thakur'},
            {'First Name': 'Raj', 'Last Name': 'Sharma'},
            {'First Name': 'Kiran', 'Last Name': 'Kamla'},
            {'First Name': 'Armaan', 'Last Name': 'Kumar'},
            {'First Name': 'Jaya', 'Last Name': 'Sharma'},
            {'First Name': 'Ingrid', 'Last Name': 'Galore'},
            {'First Name': 'Jaya', 'Last Name': 'Seth'},
            {'First Name': 'Armaan', 'Last Name': 'Dadra'},
            {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
            {'First Name': 'Aahana', 'Last Name': 'Arora'}
          ]
    print("original arr")
    [print(i) for i in dct]

    selection_sort(dct,['First Name' , 'Last Name'])
    print("sorted   arr")
    [print(i) for i in dct]