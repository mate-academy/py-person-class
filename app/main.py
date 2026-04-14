class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people_data: list) -> list:
    result = [Person(p["name"], p["age"]) for p in people_data]
    for data in people_data:
        person_obj = Person.people[data["name"]]
        if data.get("wife"):
            person_obj.wife = Person.people[data["wife"]]
        if data.get("husband"):
            person_obj.husband = Person.people[data["husband"]]
    return result
