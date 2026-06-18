class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    list_of_people = []
    for person in people:
        list_of_people.append(Person(person.get("name"), person.get("age")))

    for person in people:
        current_person = Person.people[person.get("name")]
        if person.get("wife"):
            current_person.wife = Person.people[person["wife"]]

        if person.get("husband"):
            current_person.husband = Person.people[person["husband"]]

    return list_of_people
