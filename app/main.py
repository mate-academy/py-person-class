class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people_data: list) -> list:
    people = [Person(person["name"], person["age"]) for person in people_data]
    for elem in people_data:
        wife = elem.get("wife")
        if wife:
            Person.people[elem.get("name")].wife = Person.people[wife]
        husband = elem.get("husband")
        if husband:
            Person.people[elem.get("name")].husband = Person.people[husband]
    return people
