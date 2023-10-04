class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = []
    for human in people:
        if ("wife" in human) and (human["wife"] is not None):
            person = Person(name=human["name"], age=human["age"])
            person.wife = human["wife"]
            result.append(person)
        elif ("husband" in human) and (human["husband"] is not None):
            person = Person(name=human["name"], age=human["age"])
            person.husband = human["husband"]
            result.append(person)
        else:
            person = Person(name=human["name"], age=human["age"])
            result.append(person)

    for person in result:
        if "wife" in person.__dict__:
            person.wife = Person.people[person.wife]
        elif "husband" in person.__dict__:
            person.husband = Person.people[person.husband]

    return result
