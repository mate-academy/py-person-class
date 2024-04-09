class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        # self.spouse = None
        Person.people[self.name] = self

    def __str__(self) -> str:
        return f"{self.name}, {self.age}"


def create_person_list(people: list) -> list:
    person_list = [
        Person(pers_data["name"], pers_data["age"]) for pers_data in people
    ]
    for pers in people:
        person_instance = Person.people.get(pers["name"])
        if pers.get("wife"):
            person_instance.wife = Person.people[pers["wife"]]
        if pers.get("husband"):
            person_instance.husband = Person.people[pers["husband"]]
    return person_list
