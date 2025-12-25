class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_data):
    Person.people.clear()
    person_list = []
    for person_info in people_data:
        name = person_info["name"]
        age = person_info["age"]
        person = Person(name, age)
        person_list.append(person)

    for person_info in people_data:
        name = person_info["name"]
        person = Person.people[name]

        if "wife" in person_info and person_info["wife"] in Person.people:
            person.wife = Person.people[person_info["wife"]]
        elif "husband" in person_info and person_info["husband"] in Person.people:
            person.husband = Person.people[person_info["husband"]]
    return person_list