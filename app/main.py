class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    new_people = []
    for person_dict in people:
        person = Person(person_dict['name'], person_dict['age'])
        new_people.append(person)

    for index in range(len(new_people)):
        if 'wife' in people[index].keys():
            if people[index]['wife']:
                name_wife = people[index]['wife']
                new_people[index].wife = new_people[index].people[name_wife]

        elif 'husband' in people[index].keys():
            if people[index]['husband']:
                name_husband = people[index]['husband']
                new_people[index].husband = \
                    new_people[index].people[name_husband]

    return new_people
