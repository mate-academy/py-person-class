class Person:
    people = {}
    def __init__ (self, name : str, age : int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = []

    for human in people:
        new_person = Person(human["name"], human["age"])
        wife, husband = human.get("wife"), human.get("husband")
        if wife:
            new_person.wife = wife
        if husband:
            new_person.husband = husband
        result.append(new_person)

    for person in result:
        if hasattr(person, "wife"):
            person.wife = Person.people[person.wife]
        if hasattr(person, "husband"):
            person.husband = Person.people[person.husband]

    return result
