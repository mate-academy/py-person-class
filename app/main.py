class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    for person in people:
        if person["name"] not in Person.people.keys():
            Person(person["name"], person["age"])

    for person in people:
        wife = person.get("wife")
        husband = person.get("husband")
        item = Person.people[person["name"]]

        if wife and wife in Person.people:
            item.wife = Person.people[wife]

        if husband and husband in Person.people:
            item.husband = Person.people[husband]

    return list(Person.people.values())
