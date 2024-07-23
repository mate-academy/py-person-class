class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for person in people:
        name = person.get("name")
        age = person.get("age")
        person_instance = Person(name, age)
        person_list.append(person_instance)

    for person in people:
        name = person.get("name")
        wife_name = person.get("wife")
        husband_name = person.get("husband")
        person_instance = Person.people[name]

        if wife_name:
            person_instance.wife = Person.people[wife_name]
        if husband_name:
            person_instance.husband = Person.people[husband_name]

    return person_list
