class Person:
    people = {}

    def __init__(self,
                 name: str,
                 age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        new_person = Person(person["name"], person["age"])
        person_list.append(new_person)

    for person in person_list:
        for human in people:
            if person.name == human["name"]:
                if human.get("wife") is not None:
                    person.wife = Person.people[human["wife"]]
                elif human.get("husband") is not None:
                    person.husband = Person.people[human["husband"]]
    return person_list
