class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        person_instance = Person.people[person["name"]]
        wife_name = person.get("wife")
        husband_name = person.get("husband")

        if wife_name in Person.people:
            person_instance.wife = Person.people[wife_name]
        if husband_name in Person.people:
            person_instance.husband = Person.people[husband_name]

    return person_list
