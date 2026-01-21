class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}

    person_list = []

    for person_data in people:
        name = person_data.get("name")
        age = person_data.get("age")
        if name is not None and age is not None:
            person = Person(name, age)
            person_list.append(person)

    for person_data, person in zip(people, person_list):
        wife_name = person_data.get("wife")
        husband_name = person_data.get("husband")

        if wife_name and wife_name in Person.people:
            person.wife = Person.people[wife_name]

        if husband_name and husband_name in Person.people:
            person.husband = Person.people[husband_name]

    return person_list
