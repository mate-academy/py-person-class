class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    created_person_list = []
    for person_data in people:
        name = person_data.get("name")
        age = person_data.get("age")
        if name is not None and age is not None:
            person = Person(name, age)
            created_person_list.append(person)
    for person in people:
        if person.get("wife"):
            Person.people[person["name"]].wife = Person.people[person["wife"]]
        if person.get("husband"):
            Person.people[person["name"]].husband = \
                Person.people[person["husband"]]
    return created_person_list
