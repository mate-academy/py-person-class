class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons = []
    for human in people:
        person = (Person(human["name"], human["age"]))
        satellite = "wife" if "wife" in human else "husband"
        if human[satellite] is not None:
            add_satellites(person, satellite, human[satellite])
        persons.append(person)
    return persons


def add_satellites(person: "Person",
                   satellite: str,
                   satellite_name: str) -> None:
    opposite = "husband" if satellite == "wife" else "wife"
    if satellite_name in Person.people:
        setattr(person, satellite, Person.people[satellite_name])
        setattr(Person.people[satellite_name], opposite, person)
