class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    people_instance = [Person(person["name"], person["age"])
                       for person in people
                       ]
    for value, person in enumerate(people):
        if person.get("wife") is not None:
            people_instance[value].wife = Person.people[person["wife"]]
        if person.get("husband") is not None:
            people_instance[value].husband \
                = Person.people[person["husband"]]
    return people_instance
