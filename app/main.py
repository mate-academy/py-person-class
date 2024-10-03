class Person:
    people: {str, "Person"} = {}

    def __init__(self, name: str = None, age: int = None) -> None:
        self.name = name
        self.age = age
        Person.people.update({name: self})


def create_person_list(people: list) -> list:
    person_list = [Person(person.get("name"),
                          person.get("age")) for person in people]
    for i in range(len(people)):
        if people[i].get("wife"):
            person_list[i].wife = Person.people.get(people[i].get("wife"))
        if people[i].get("husband"):
            person_list[i].husband = Person.people.get(
                people[i].get("husband"))
    return person_list
