##reverse a string
string = "qwerty uiop asdfg hjkl"
string_array = [i for i in string.split()]
print([string_array[(-1*(i+1))] for i in range(0,len(string_array))])
print(string_array[::-1])
print([i[::-1] for i in string_array[::-1]])
print(string[::-1].split())

for x in range(1,101):
    prime = False
    for y in range(2,x):
        if x%y==0:
            break
        else:
            prime = True
    if prime:
        print (x,sep=' ', end=' ')