class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for info in people:
        person_list.append(Person(info["name"], info["age"]))

    for info in people:
        current_name = info["name"]
        current_person = Person.people[current_name]
        if "husband" in info and info["husband"] is not None:
            husband_name = info["husband"]
            current_person.husband = Person.people[husband_name]
        if "wife" in info and info["wife"] is not None:
            wife_name = info["wife"]
            current_person.wife = Person.people[wife_name]

    return person_list


