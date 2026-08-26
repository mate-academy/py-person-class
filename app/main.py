class Person:
    people = {}
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people) -> list[Person]:
    person_list = []

    for person in people:
        new_person = Person(person["name"], person["age"])
        person_list.append(new_person)

    for person in people:
        person_instance = Person.people[person["name"]]

        if person.get("wife") is not None:
            person_instance.wife = Person.people[person["wife"]]

        if person.get("husband") is not None:
            person_instance.husband = Person.people[person["husband"]]

    return person_list

