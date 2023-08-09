class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons_list = [Person(friend["name"], friend["age"]) for friend in people]
    for frd in people:
        if frd.get("wife"):
            Person.people[frd["name"]].wife = Person.people[frd["wife"]]
        if frd.get("husband"):
            Person.people[frd["name"]].husband = Person.people[frd["husband"]]
    return persons_list
