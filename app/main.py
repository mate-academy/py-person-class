class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> None:
    person_list = []

    for person_dict in people:
        name = person_dict["name"]
        age = person_dict["age"]

        person = Person(name, age)
        person_list.append(person)

    for person_dict in people:
        name = person_dict["name"]
        if "wife" in person_dict and person_dict["wife"] is not None:
            # Установка атрибута wife
            wife_name = person_dict["wife"]
            Person.people[name].wife = Person.people[wife_name]
        elif "husband" in person_dict and person_dict["husband"] is not None:
            # Установка атрибута husband
            husband_name = person_dict["husband"]
            Person.people[name].husband = Person.people[husband_name]

    return person_list
