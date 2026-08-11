class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    list_of_persons = [Person(p["name"], p["age"]) for p in people]

    for person_data in people:
        if person_data.get("wife"):
            wife = Person.people[person_data["wife"]]
            Person.people[person_data["name"]].wife = wife
        if person_data.get("husband"):
            husband = Person.people[person_data["husband"]]
            Person.people[person_data["name"]].husband = husband
    return list_of_persons
