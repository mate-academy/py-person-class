class Person:
    people = {}

    def __init__(self, name: str, age: int, **kwargs) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    people_objs = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        human = Person.people[person["name"]]

        if person.get("husband") is not None:
            husband = Person.people[person["husband"]]
            human.husband = husband
            husband.wife = human
        elif person.get("wife") is not None:
            wife = Person.people[person["wife"]]
            human.wife = wife
            wife.husband = human

    return people_objs
