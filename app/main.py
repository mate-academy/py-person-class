class Person:
    people = {}

    def __init__(self, name: str, age: int, **kwargs):
        self.name = name
        self.age = age
        if "wife" in kwargs:
            self.add_satellite("wife", kwargs["wife"])
        if "husband" in kwargs:
            self.add_satellite("husband", kwargs["husband"])
        Person.people[name] = self

    def add_satellite(self, satellite: str, satellite_name: str) -> None:
        person = Person.people[satellite_name] \
            if satellite_name in Person.people else None
        setattr(self, satellite, person)
        opposite = "husband" if satellite == "wife" else "wife"
        if satellite_name in Person.people:
            setattr(Person.people[satellite_name], opposite, self)


def create_person_list(people: list) -> list:
    persons = []
    for human in people:
        if "wife" in human:
            if human["wife"] is None:
                persons.append(Person(human["name"], human["age"]))
            else:
                persons.append(Person(human["name"],
                                      human["age"],
                                      wife=human["wife"]))
        if "husband" in human:
            if human["husband"] is None:
                persons.append(Person(human["name"], human["age"]))
            else:
                persons.append(Person(human["name"],
                                      human["age"],
                                      husband=human["husband"]))
    return persons
