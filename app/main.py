class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    list_of_people = [
        Person(person_info["name"], person_info["age"])
        for person_info in people
    ]
    for index, info in enumerate(people):
        if info.get("wife"):
            list_of_people[index].wife = Person.people[info.get("wife")]
        if info.get("husband"):
            list_of_people[index].husband = Person.people[info.get("husband")]
    return list_of_people
