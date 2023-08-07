class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.add_instance()
        self.people[name] = self

    def add_instance(self) -> None:
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    persons_list = []
    for i in people:
        name_instance = Person(i["name"], i["age"])
        persons_list.append(name_instance)
    for character in people:
        if character.get("wife"):
            Person.people[character["name"]].wife = Person.people[character["wife"]]
        if character.get("husband"):
            Person.people[character["name"]].husband = Person.people[character["husband"]]

    return persons_list
