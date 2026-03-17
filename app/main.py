class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}
    persons = []

    for data in people:
        person = Person(data["name"], data["age"])
        persons.append(person)

    for data in people:
        person = Person.people[data["name"]]

        wife_name = data.get("wife")
        if wife_name is not None:
            person.wife = Person.people[wife_name]

        husband_name = data.get("husband")
        if husband_name is not None:
            person.husband = Person.people[husband_name]

    return persons
