class Person:
    people = dict()

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    new_list = list()
    for x in people:
        obj = Person(x['name'], x['age'])
        new_list.append(obj)

    for n, i in enumerate(people):
        if 'wife' in i.keys() and i['wife'] is not None:
            setattr(new_list[n], 'wife', Person.people[i['wife']])
        elif 'husband' in i.keys() and i['husband'] is not None:
            setattr(new_list[n], 'husband', Person.people[i['husband']])
    return new_list
