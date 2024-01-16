class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[name] = self


def create_person_list(people_list: list) -> list:
    persons = []

    for human in people_list:
        name = human["name"]
        age = human["age"]
        person = Person(name, age)
        persons.append(person)

    for person in people_list:
        if person.get("wife"):
            way_to_person = Person.people[person["name"]]
            way_to_person.wife = Person.people[person["wife"]]
        if "husband" in person:
            if person["husband"] is not None:

                way_to_person = Person.people[person["name"]]
                way_to_person.husband = Person.people[person["husband"]]
    return persons
