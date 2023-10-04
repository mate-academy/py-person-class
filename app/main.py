class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result_list = [Person(person["name"], person["age"]) for person in people]
    for pers in people:
        if pers.get("wife"):
            Person.people[pers.get("wife")].husband \
                = Person.people[pers["name"]]
            Person.people[pers["name"]].wife \
                = Person.people[pers.get("wife")]
        elif pers.get("husband"):
            Person.people[pers.get("husband")].wife \
                = Person.people[pers["name"]]
            Person.people[pers["name"]].husband \
                = Person.people[pers.get("husband")]

    return result_list
