# student={'Archana':28,'krishna':25,'Ramesh':32,'vineeth':25}
# def test(student):
#     new={'alok':30,'Nevadan':28}
#     student.update(new)
#     print("Inside the function",student)
#     return
# test(student)
# print("outside the function",student)

def call_by_value():
    String = 'morning'
    def data(string):
        string = 'Good Morning'
        print('Inside the Function',string)
    data(string)
    print('Outside the Function',string)

def call_by_reference():
    def data(string):
        string = 'Good Morning'
        print('Inside the Function',string)
    data(string)
    print('Outside the Function',string)

call_by_value()
call_by_reference()