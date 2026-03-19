class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    [Person(person["name"], person["age"]) for person in people]

    for person in people:
        if person.get("wife"):
            wife_name = Person.people[person["name"]]
            wife_name.wife = Person.people[person["wife"]]

        if person.get("husband"):
            husband_name = Person.people[person["name"]]
            husband_name.husband = Person.people[person["husband"]]

    return list(Person.people.values())
