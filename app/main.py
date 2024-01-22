class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[name] = self


def create_person_list(people: str) -> None:
    person_list = []

    for person_data in people:
        person = Person(person_data["name"], person_data["age"])
        person_list.append(person)

    for person_data in people:
        person = Person.people[person_data["name"]]
        if "wife" in person_data and person_data["wife"] is not None:
            person.wife = Person.people.get(person_data["wife"], None)
        if "husband" in person_data and person_data["husband"] is not None:
            person.husband = Person.people.get(person_data["husband"], None)

    return person_list
