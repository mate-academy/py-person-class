class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_instances = []

    for person in people:
        person_name = person["name"]
        person_age = person["age"]
        person_instance = Person(person_name, person_age)
        person_instances.append(person_instance)

    for person in people:
        person_name = person["name"]
        if person.get("wife") is not None:
            wife = person.get("wife")
            Person.people[person_name].wife = Person.people[wife]
        if person.get("husband") is not None:
            husband = person.get("husband")
            Person.people[person_name].husband = Person.people[husband]
    return person_instances
