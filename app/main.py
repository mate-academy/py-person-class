class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:

    list_of_people = []

    for data in people:
        person_inst = Person(data["name"], data["age"])
        list_of_people.append(person_inst)

    for data in people:
        for names in Person.people.keys():
            if "wife" in data and data["wife"] == names:
                Person.people[data["name"]].wife = Person.people[names]
            elif "husband" in data and data["husband"] == names:
                Person.people[data["name"]].husband = Person.people[names]

    return list_of_people
