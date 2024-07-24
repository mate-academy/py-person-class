class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        Person.people[name] = self


def create_person_list(people_data: list) -> list:
    class_list = []
    for person_data in people_data:
        class_list.append(Person(person_data["name"], person_data["age"]))

    for i, person_data in enumerate(people_data):
        if person_data.get("wife") is not None:
            class_list[i].wife = Person.people[person_data["wife"]]
        else:
            delattr(class_list[i], "wife")

        if person_data.get("husband") is not None:
            class_list[i].husband = Person.people[person_data["husband"]]
        else:
            delattr(class_list[i], "husband")

    return class_list
