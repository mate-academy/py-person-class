class Person:
    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age

        self.people[name] = self


def create_person_list(people_data: list) -> list:
    people_list = [Person(pers["name"], pers["age"]) for pers in people_data]

    for pers in people_data:
        if pers.get("wife"):
            Person.people[pers["name"]].wife = Person.people[pers["wife"]]
            Person.people[pers["wife"]].husband = Person.people[pers["name"]]

        elif pers.get("husband"):
            Person.people[pers["name"]].husband = (
                Person.people[pers["husband"]])
            Person.people[pers["husband"]].wife = Person.people[pers["name"]]

    return people_list
