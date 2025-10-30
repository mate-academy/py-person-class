class Person:

    people = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people_dicts: list) -> list:
    person_list = []
    for data in people_dicts:
        person = Person(data["name"], data["age"])
        person_list.append(person)
    for data in people_dicts:
        person_instance = Person.people[data["name"]]
        if "wife" in data and data["wife"] is not None:
            wife_name = data["wife"]
            person_instance.wife = Person.people[wife_name]
        elif "husband" in data and data["husband"] is not None:
            husband_name = data["husband"]
            person_instance.husband = Person.people[husband_name]

    return person_list
