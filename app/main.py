class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        # store people by {name: person_object}
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    people_list = [Person(person["name"], person["age"]) for person in people]
    for person in people:
        name = person["name"]
        spouse_name = person.get("husband") or person.get("wife")
        if person.get("husband"):
            Person.people[name].husband = Person.people[spouse_name]
        elif person.get("wife"):
            Person.people[name].wife = Person.people[spouse_name]

    return people_list
