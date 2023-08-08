class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons_list = []
    name_instance = [persons_list.append(Person(friend["name"], friend["age"])) for friend in people]

    for character in people:
        if character.get("wife"):
            Person.people[character["name"]].wife = Person.people[character["wife"]]
        if character.get("husband"):
            Person.people[character["name"]].husband = Person.people[character["husband"]]
    return persons_list
