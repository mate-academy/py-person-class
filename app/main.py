class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for human in people:
        new_person = Person(human["name"], human["age"])
        person_list.append(new_person)
    for human in people:
        human_instance = Person.people[human["name"]]
        if human.get("wife"):
            wife = Person.people[human["wife"]]
            human_instance.wife = wife
        if human.get("husband"):

            husband = Person.people[human["husband"]]
            human_instance.husband = husband
    return person_list
