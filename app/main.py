class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    list_of_people = [
        Person(name=person["name"], age=person["age"],)
        for person in people
    ]

    for i, person_obj in enumerate(list_of_people):
        if "wife" in people[i].keys():
            if people[i]["wife"] is not None:
                person_obj.wife = Person.people[people[i]["wife"]]

        elif "husband" in people[i].keys():
            if people[i]["husband"] is not None:
                person_obj.husband = Person.people[people[i]["husband"]]

    return list_of_people
