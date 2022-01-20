class Person:
    people = dict()

    def __init__(self, name, age, *args):
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons = [Person(person["name"], person["age"]) for person in people]
    for person in people:
        wife = person.get('wife')
        husband = person.get('husband')
        if wife:
            wife = Person.people[wife]
            Person.people[person['name']].wife = wife
        if husband:
            husband = Person.people[husband]
            Person.people[person['name']].husband = husband

    return persons
