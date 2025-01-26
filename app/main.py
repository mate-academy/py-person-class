class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person_data in people:
        name = person_data["name"]
        age = person_data["age"]
        person_instance = Person(name, age)
        person_list.append(person_instance)

    for person_data in people:
        name = person_data["name"]
        instance = Person.people[name]

        if "wife" in person_data and person_data["wife"]:
            instance.wife = Person.people[person_data["wife"]]
        elif "husband" in person_data and person_data["husband"]:
            instance.husband = Person.people[person_data["husband"]]

    return person_list
