class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        name = person["name"]
        age = person["age"]
        person = Person(name, age)
        person_list.append(person)

    for person in people:
        if person.get("wife"):
            wife_name = Person.people[person["wife"]]
            Person.people[person["name"]].wife = wife_name

        if person.get("husband"):
            husband_name = Person.people[person["husband"]]
            Person.people[person["name"]].husband = husband_name
    return person_list
