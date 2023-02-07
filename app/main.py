class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    persons_list = [Person(person["name"], person["age"]) for person in people]
    for name, person in Person.people.items():
        for personal_info in people:
            if personal_info.get("wife") and name == personal_info["name"]:
                person.wife = Person.people[personal_info["wife"]]
            if personal_info.get("husband") and name == personal_info["name"]:
                person.husband = Person.people[personal_info["husband"]]
    return persons_list
