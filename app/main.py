class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list[Person]:
    people_instances = [
        Person(human.get("name"), human.get("age"))
        for human in people
    ]
    for person in people:
        person_instance = Person.people.get(person.get("name"))
        if wife_name := person.get("wife"):
            person_instance.wife = Person.people.get(wife_name)
        if husband_name := person.get("husband"):
            person_instance.husband = Person.people.get(husband_name)
    return people_instances
