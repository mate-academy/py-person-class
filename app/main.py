class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

        Person.people[name] = self

def create_person_list(people: list) -> list:
    Person.people.clear()
    person_list = []

    for person_info in people:
        person = Person(name=person_info["name"], age=person_info["age"])
        person_list.append(person)

    for person_info in people:
        person = Person.people[person_info["name"]]

        if "wife" in person_info and person_info["wife"] is not None:
            person.wife = Person.people[person_info["wife"]]
        elif "husband" in person_info and person_info["husband"] is not None:
            person.husband = Person.people[person_info["husband"]]

    return person_list

