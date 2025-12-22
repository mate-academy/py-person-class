class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self
    pass


def create_person_list(people: list) -> list:
    person_list = [Person(element["name"], element["age"])
                   for element in people]
    for person in person_list:
        for person_dict in people:
            if person.name == person_dict["name"]:
                if person_dict.get("wife") is not None:
                    person.wife = Person.people[person_dict.get("wife")]
                if person_dict.get("husband") is not None:
                    person.husband = Person.people[person_dict.get("husband")]
    return person_list
