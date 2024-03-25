class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        wife_name = person.get("wife")
        husband_name = person.get("husband")
        current_person = Person.people[person["name"]]

        if wife_name:
            current_person.wife = Person.people[wife_name]
        if husband_name:
            current_person.husband = Person.people[husband_name]

    return person_list
