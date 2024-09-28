class Person:
    people = {}

    def __init__(self, name: str, age: int):

        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        human_name = Person.people[person["name"]]

        wife = person.get("wife")
        husband = person.get("husband")

        if wife:
            human_name.wife = Person.people[wife]

        if husband:
            human_name.husband = Person.people[husband]

    return person_list
