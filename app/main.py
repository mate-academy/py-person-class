class Person:
    people = {}

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None

        Person.people[name] = self


def create_person_list(people_list: list) -> list:
    for person_data in people_list:
        name = person_data["name"]
        age = person_data["age"]
        Person(name=name, age=age)

    for person_data in people_list:
        name = person_data["name"]
        person = Person.people[name]

        if "wife" in person_data and person_data["wife"] is not None:
            wife_name = person_data["wife"]
            person.wife = Person.people[wife_name]
        else:
            if hasattr(person, "wife"):
                del person.wife

        if "husband" in person_data and person_data["husband"] is not None:
            husband_name = person_data["husband"]
            person.husband = Person.people[husband_name]
        else:
            if hasattr(person, "husband"):
                del person.husband

    return list(Person.people.values())
