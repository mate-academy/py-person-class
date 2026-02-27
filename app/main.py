class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    Person.people.clear()
    for person_data in people:
        name = person_data["name"]
        age = person_data["age"]
        new_person = Person(name, age)
        person_list.append(new_person)

    for person_data in people:
        name = person_data["name"]
        current_person = Person.people[name]

        if "wife" in person_data and person_data["wife"] is not None:
            wife_name = person_data["wife"]
            current_person.wife = Person.people[wife_name]

        if "husband" in person_data and person_data["husband"] is not None:
            husband_name = person_data["husband"]
            current_person.husband = Person.people[husband_name]

    return person_list
