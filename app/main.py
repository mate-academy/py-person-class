class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = list()

    for person_data in people:
        person_instance = Person(person_data["name"], person_data["age"])
        person_list.append(person_instance)

    for person_instance, person_data in zip(person_list, people):
        if "wife" in person_data and person_data["wife"]:
            person_instance.wife = Person.people[person_data["wife"]]
        elif "husband" in person_data and person_data["husband"]:
            person_instance.husband = Person.people[person_data["husband"]]

    return person_list
