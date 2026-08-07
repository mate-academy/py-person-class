class Person:
    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    nlist = [Person(di["name"], di["age"]) for di in people]
    for di, cls in zip(people, nlist):  # di == dict cls == class(Person)
        if di.get("wife") is not None:
            cls.wife = Person.people.get(di.get("wife"))
        if di.get("husband") is not None:
            cls.husband = Person.people.get(di.get("husband"))
    return nlist
