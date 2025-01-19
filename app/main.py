class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_dicts: list) -> list:
    person_list = []
    for person_dict in people_dicts:
        person = Person(name=person_dict["name"], age=person_dict["age"])
        person_list.append(person)

    for person_dict in people_dicts:
        name = person_dict["name"]
        instance = Person.people[name]

        if "wife" in person_dict and person_dict["wife"]:
            instance.wife = Person.people[person_dict["wife"]]
        elif "husband" in person_dict and person_dict["husband"]:
            instance.husband = Person.people[person_dict["husband"]]

    return person_list
