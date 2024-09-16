class Person:
    people = {}

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        Person.people[name] = self


def create_person_list(people: list) -> list:
    name_to_person = {}
    person_list = []

    for person_data in people:
        name = person_data["name"]
        age = person_data["age"]

        person = Person(name, age)
        name_to_person[name] = person
        person_list.append(person)

    for person_data in people:
        person = name_to_person[person_data["name"]]
        if person_data.get("wife") is not None:
            person.wife = name_to_person.get(person_data["wife"])
        else:
            if hasattr(person, "wife"):
                del person.wife

        if person_data.get("husband") is not None:
            person.husband = name_to_person.get(person_data["husband"])
        else:
            if hasattr(person, "husband"):
                del person.husband

    return person_list
