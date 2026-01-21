class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self

    def __repr__(self) -> str:
        return f"Person({self.__dict__})"


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]
    for person in people:
        wife_name = person.get("wife")
        if wife_name is not None:
            man = Person.people[person["name"]]
            wife = Person.people[person["wife"]]
            man.wife = wife
        husband_name = person.get("husband")
        if husband_name is not None:
            woman = Person.people[person["name"]]
            husband = Person.people[person["husband"]]
            woman.husband = husband
    return person_list
