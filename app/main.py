class Person:
    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        human = Person(person["name"], person["age"])

        person_list.append(human)

    for index, person in enumerate(people):
        if person.get("wife"):
            for human in person_list:
                if human.name == person.get("wife"):
                    person_list[index].wife = human

        if person.get("husband"):

            for human in person_list:
                if human.name == person.get("husband"):
                    person_list[index].husband = human

    return person_list
