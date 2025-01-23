class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        person_proto = Person(person["name"], person["age"])

        if "wife" in person and person["wife"] is not None:
            person_proto.wife = Person.people.get(
                person["wife"], Person(person["wife"], 0))
            person_proto.wife.husband = person_proto
        elif "husband" in person and person["husband"] is not None:
            person_proto.husband = Person.people.get(
                person["husband"], Person(person["husband"], 0))
            person_proto.husband.wife = person_proto

        person_list.append(person_proto)
    return person_list
