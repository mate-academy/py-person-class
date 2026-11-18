class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    people_list = [Person(person["name"], person["age"]) for person in people]

    for person, data in zip(people_list, people):
        if data.get("wife"):
            wife = data.get("wife")
            person.wife = Person.people[wife]
        elif data.get("husband"):
            husband = data.get("husband")
            person.husband = Person.people[husband]

    return people_list
