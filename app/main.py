class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    persons_list = [Person(person["name"], person["age"]) for person in people]
    for person in people:
        wife = person.get("wife")
        husband = person.get("husband")
        personal_info = Person.people[person.get("name")]
        if wife:
            personal_info.wife = Person.people[wife]
        if husband:
            personal_info.husband = Person.people[husband]
    return persons_list
