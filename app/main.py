class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_list: list) -> list:
    person_list = []
    for human in people_list:
        person = Person(human["name"], human["age"])
        person_list.append(person)

    for human in people_list:
        if human.get("wife"):
            Person.people[human["name"]].wife = Person.people[human["wife"]]
        if human.get("husband"):
            husband_link = Person.people[human["husband"]]
            Person.people[human["name"]].husband = husband_link
    return person_list
