class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    created = [Person(person_data["name"], person_data["age"])
               for person_data in people]
    for person in people:
        name = person["name"]
        if person.get("wife") is not None:
            wife = person["wife"]
            Person.people[name].wife = Person.people[wife]
            Person.people[wife].husband = Person.people[name]
        if person.get("husband") is not None:
            husband = person["husband"]
            Person.people[name].husband = Person.people[husband]
            Person.people[husband].wife = Person.people[name]
    return created
