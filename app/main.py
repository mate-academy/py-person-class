class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    peoples_lst = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        if person.get("wife") is not None:
            wife = Person.people[person.get("wife")]
            Person.people[person.get("name")].wife = wife
        if person.get("husband") is not None:
            husband = Person.people[person.get("husband")]
            Person.people[person.get("name")].husband = husband

    return peoples_lst
