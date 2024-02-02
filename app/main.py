class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    list_of_people = [
        Person(name=human["name"], age=human["age"])
        for human in people
    ]
    for human in people:
        if human.get("wife"):
            Person.people[human.get("name")].wife\
                = Person.people[human.get("wife")]
        if human.get("husband"):
            Person.people[human.get("name")].husband\
                = Person.people[human.get("husband")]
    return list_of_people
