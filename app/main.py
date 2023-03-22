class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict[str, [str | int]]]) -> list[Person]:
    person_list = [
        Person(human["name"], human["age"])
        for human in people
    ]
    for index_person, person in enumerate(people):
        if person.get("wife"):
            person_list[index_person].wife = (
                Person.people[person["wife"]]
            )
        if person.get("husband"):
            person_list[index_person].husband = (
                Person.people[person["husband"]]
            )

    return person_list
