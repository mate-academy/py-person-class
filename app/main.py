class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    peoples_dict = [
        Person(name=human["name"],
               age=human["age"])
        for human in people
    ]

    for human in people:
        if human.get("wife"):
            Person.people[human["name"]].wife = (
                Person.people.get(human["wife"])
            )
        if human.get("husband"):
            Person.people[human["name"]].husband = (
                Person.people.get(human["husband"])
            )

    return peoples_dict
