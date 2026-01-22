class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]

    for person_data, person_instance in zip(people, person_list):
        if "wife" in person_data:
            if person_data["wife"] in Person.people:
                person_instance.wife = Person.people[person_data["wife"]]
        elif "husband" in person_data:
            if person_data["husband"] in Person.people:
                person_instance.husband = Person.people[person_data["husband"]]

    return person_list
