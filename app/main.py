class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    [Person(person["name"], person["age"]) for person in people]

    for person in people:
        person_instance = Person.people.get(person["name"])

        if wife_name := person.get("wife"):
            Person.people.get(wife_name).husband = person_instance
        elif husband_name := person.get("husband"):
            Person.people.get(husband_name).wife = person_instance

    return list(Person.people.values())
