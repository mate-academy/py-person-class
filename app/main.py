class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.age = age
        self.name = name
        Person.people[name] = self


def create_person_list(people: list) -> list:
    all_people = [
        Person(details["name"], details["age"]) for details in people
    ]
    for i, person_info in enumerate(people):
        if person_info.get("wife"):
            all_people[i].wife = person_info["wife"]
            all_people[i].wife = Person.people[person_info["wife"]]
        elif person_info.get("husband"):
            all_people[i].husband = person_info["husband"]
            all_people[i].husband = Person.people[person_info["husband"]]
    return all_people
