class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

    def __repr__(self) -> str:
        return str(self.__dict__)


def create_person_list(people: list) -> list:
    people_list = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        if person.get("wife"):
            husband = Person.people.get(person.get("name"))
            wife = Person.people.get(person.get("wife"))
            husband.wife = wife
        if person.get("husband"):
            wife = Person.people.get(person.get("name"))
            husband = Person.people.get(person.get("husband"))
            wife.husband = husband

    return people_list
