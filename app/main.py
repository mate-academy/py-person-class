class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person_dict in people:
        person = Person(person_dict["name"], person_dict["age"])
        person_list.append(person)
        if person_dict.get("wife") is not None:
            person.wife = person_dict["wife"]
        if person_dict.get("husband") is not None:
            person.husband = person_dict["husband"]
    return person_list
