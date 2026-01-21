class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person_data["name"], person_data["age"])
                   for person_data in people]

    for index, person_data in enumerate(people):
        if person_data.get("wife"):
            person_list[index].wife = Person.people[person_data["wife"]]
        if person_data.get("husband"):
            person_list[index].husband = Person.people[person_data["husband"]]

    return person_list
