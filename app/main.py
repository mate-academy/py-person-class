class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    list_of_people = [
        Person(person_info["name"], person_info["age"]) for person_info in people
    ]

    for index, person_info in enumerate(people):
        if person_info.get("wife"):
            list_of_people[index].wife = Person.people.get(person_info["wife"])
        if person_info.get("husband"):
            list_of_people[index].husband = Person.people.get(person_info["husband"])
    return list_of_people
