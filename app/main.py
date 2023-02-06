class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]
    for name, person in Person.people.items():
        for person_info in people:
            if name == person_info["name"] and person_info.get("wife"):
                person.wife = Person.people[person_info["wife"]]
            if name == person_info["name"] and person_info.get("husband"):
                person.husband = Person.people[person_info["husband"]]
    return person_list

