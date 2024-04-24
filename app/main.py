class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    persons_list = []

    for human in people:
        persons_list.append(Person(human["name"], human["age"]))

    for human in people:
        if human.get("wife"):
            wife_name = Person.people[human.get("wife")]
            Person.people[human.get("name")].wife = wife_name
        elif human.get("husband"):
            husband_name = Person.people[human.get("husband")]
            Person.people[human.get("name")].husband = husband_name

    return persons_list
