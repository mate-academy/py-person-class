class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[self.name] = self


def create_person_list(people: list) -> list:
    created_people = []
    for person_data in people:
        person = Person(person_data["name"], person_data["age"])
        created_people.append(person)

    for person_data in people:
        if "wife" in person_data and person_data["wife"] is not None:
            name = person_data["name"]
            wife = person_data["wife"]
            Person.people[name].wife = Person.people[wife]
            Person.people[wife].husband = Person.people[name]

    return created_people
