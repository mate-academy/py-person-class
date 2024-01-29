class Person:
    people = dict()

    def __init__(self,
                 name: str,
                 age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"])
                   for person in people]
    instance = Person.people
    for person in people:
        if person.get("wife"):
            instance[person["name"]].wife = instance[person["wife"]]
        elif person.get("husband"):
            instance[person["name"]].husband = instance[person["husband"]]
    return person_list
