class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    all_persons = [Person(human["name"], human["age"]) for human in people]

    for human in people:

        if human.get("wife"):
            wife_obj = Person.people[human["wife"]]
            Person.people[human["name"]].wife = wife_obj

        elif human.get("husband"):
            husband_obj = Person.people[human["husband"]]
            Person.people[human["name"]].husband = husband_obj

    return all_persons
