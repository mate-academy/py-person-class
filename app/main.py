class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    [Person(person["name"], person["age"]) for person in people]
    for person in people:
        Person(person["name"], person["age"])
        if person.get("wife"):
            wife = Person.people[person["wife"]]
            husband = Person.people[person["name"]]
            husband.wife, wife.husband = wife, husband
    return list(Person.people.values())
