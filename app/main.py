class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        person_list.append(Person(person["name"], person["age"]))
    for person in person_list:
        for somebody in people:
            if person.name == somebody["name"]:
                for key in somebody:
                    if key == "wife" and somebody["wife"] is not None:
                        person.wife = Person.people[somebody["wife"]]
                    elif key == "husband" and somebody["husband"] is not None:
                        person.husband = Person.people[somebody["husband"]]
    return person_list
