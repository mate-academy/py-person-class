class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    list_p = []
    for person in people:
        person_unit = Person(person["name"], person["age"])
        list_p.append(person_unit)

    for people_dict, person in zip(people, list_p):
        if people_dict.get("wife") is not None:
            person.wife = Person.people[people_dict.get("wife")]
        if people_dict.get("husband") is not None:
            person.husband = Person.people[people_dict.get("husband")]

    return list_p
