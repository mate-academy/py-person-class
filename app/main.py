class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self
        self.wife = None
        self.husband = None


def create_person_list(people: list) -> list:
    person_list = []
    for person_data in people:
        name = person_data["name"]
        age = person_data["age"]
        person = Person(name, age)

        if "wife" in person_data and person_data["wife"] is not None:
            wife_name = person_data["wife"]
            if wife_name in Person.people:
                person.wife = Person.people[wife_name]

        if "husband" in person_data and person_data["husband"] is not None:
            husband_name = person_data["husband"]
            if husband_name in Person.people:
                person.husband = Person.people[husband_name]

        person_list.append(person)

    return person_list
