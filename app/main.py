class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    Person.people = {}
    [Person(item["name"], item["age"]) for item in people]

    for item in people:
        person = Person.people[item["name"]]

        wife = item.get("wife")
        if wife:
            person.wife = Person.people[wife]

        husband = item.get("husband")
        if husband:
            person.husband = Person.people[husband]
    return list(Person.people.values())
