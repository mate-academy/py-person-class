class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(peoples: list) -> list:
    new_list = [Person(people["name"], people["age"]) for people in peoples]

    for people in peoples:
        if people.get("wife"):
            Person.people[people["name"]].wife = Person.people[people["wife"]]
        elif people.get("husband"):
            Person.people[
                people["name"]].husband = Person.people[people["husband"]]

    return new_list
