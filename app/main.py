class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    # write your code here
    print(len(people))
    person_list = []
    for person in people:
        if "wife" in person and person['wife'] != None:
            name = Person(person["name"], person["age"])
            name.wife = person['wife']

            person_list.append(name)
            continue
        if "husband" in person and person['husband'] != None:
            name = Person(person["name"], person["age"])
            name.husband = person['husband']

            person_list.append(name)
            continue
        else:
            name = Person(person["name"], person["age"])
            person_list.append(name)
    for person in people:
        persona = Person.people[person['name']]
        if 'wife' in person and person['wife'] is not None:
            persona.wife = Person.people[person['wife']]

        if 'husband' in person and person['husband'] is not None:
            persona.husband = Person.people[person['husband']]
    return person_list

