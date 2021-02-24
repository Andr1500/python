# creare record in function with dictionary

def create_record(name, phone, address):
    """create record"""
    record = {
        'name': name,
        'phone': phone,
        'address': address
    }

    return record

user1 = create_record('Vasua', '2344', 'Aswig')
user2 = create_record('Boris', '2345', 'Zulkin')

print(user1)
print(user2)

#print defined people with specific parameters, * (in *people) meaning multiple choises

def avards(medal, *people):
    """give medals for something"""
    for person in people:
        print(person.title() + " avards of medal " + medal)

avards('the best', 'Vasia', 'Zbych')
avards('Very attractive', 'Valia', 'Vera')
