class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:

    Person.people = {}
    list_of_people = []

    for person in people:
        current = Person(person["name"], person["age"])

        wife = person.get("wife")
        if wife and wife in Person.people:
            current.wife = Person.people[wife]
            Person.people[wife].husband = current

        husband = person.get("husband")
        if husband and husband in Person.people:
            current.husband = Person.people[husband]
            Person.people[husband].wife = current

        list_of_people.append(current)

    return list_of_people
