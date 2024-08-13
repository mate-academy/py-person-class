class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for person_dict in people:
        person_list.append(Person(person_dict["name"], person_dict["age"]))

    for person_dict in people:
        if "wife" in person_dict and person_dict["wife"]:
            Person.people[person_dict["name"]].wife\
                = Person.people[person_dict["wife"]]
        elif "husband" in person_dict and person_dict["husband"]:
            Person.people[person_dict["name"]].husband\
                = Person.people[person_dict["husband"]]

    return person_list
