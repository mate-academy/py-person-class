class Person:
    people = {}

    def __init__(self, name, age, wife=None, husband=None):
        self.name = name
        self.age = age
        self.wife = wife
        self.husband = husband
        Person.people[name] = self


def create_person_list(people: list) -> list:
    res_list = []

    for el in people:
        person = Person(el["name"], el["age"], el.get("wife"), el.get("husband"))
        res_list.append(person)

    for person in res_list:
        if person.wife:
            person.wife = Person.people.get(person.wife)
        elif person.husband:
            person.husband = Person.people.get(person.husband)

    return res_list

