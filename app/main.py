class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person_info in people:
        person = Person(person_info["name"], person_info["age"])
        person_list.append(person)

    for person_info in people:
        person = Person.people[person_info["name"]]
        if "wife" in person_info and person_info["wife"]:
            person.wife = Person.people[person_info["wife"]]
        elif "husband" in person_info and person_info["husband"]:
            person.husband = Person.people[person_info["husband"]]
        else:
            del person.wife
            del person.husband
    return person_list
