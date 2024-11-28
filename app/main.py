class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    ext_list = []
    for pers_dict in people:
        person = Person(pers_dict["name"], pers_dict["age"])
        ext_list.append(person)

    for pers_dict in people:
        person = Person.people[pers_dict["name"]]
        if "wife" in pers_dict and pers_dict["wife"] is not None:
            person.wife = Person.people.get(pers_dict["wife"])
        elif "husband" in pers_dict and pers_dict["husband"] is not None:
            person.husband = Person.people.get(pers_dict["husband"])

    return ext_list
