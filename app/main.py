class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    list_of_completed_people = [
        Person(person["name"], person["age"])
        for person in people
    ]

    for index, person in enumerate(people):
        if person.get("wife"):
            wife = Person.people[person["wife"]]
            list_of_completed_people[index].wife = wife
        if person.get("husband"):
            husband = Person.people[person["husband"]]
            list_of_completed_people[index].husband = husband

    return list_of_completed_people
