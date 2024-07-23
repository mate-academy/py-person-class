class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    list_person = []
    names = {}
    for human in people:
        person = Person(human["name"], human["age"])
        list_person.append(person)
        names[human["name"]] = person

    for human in people:
        person = names[human["name"]]
        if "wife" in human and human["wife"] is not None:
            if human["wife"] in names:
                person.wife = names[human["wife"]]
        if "husband" in human and human["husband"] is not None:
            if human["husband"] in names:
                person.husband = names[human["husband"]]

    return list_person
