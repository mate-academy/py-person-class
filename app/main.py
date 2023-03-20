class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person_dict in people:
        person = Person(person_dict["name"], person_dict["age"])
        Person.people[person_dict["name"]] = person
        person_list.append(person)
    for person_dict in people:
        person = Person.people[person_dict["name"]]
        if person_dict.get("wife") is not None:
            person.wife = Person.people[person_dict["wife"]]
        elif person_dict.get("husband") is not None:
            person.husband = Person.people[person_dict["husband"]]
    return person_list
