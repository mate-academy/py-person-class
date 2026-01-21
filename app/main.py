class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(persons: list) -> list:
    list_of_people = []
    for person in persons:
        new_person = Person(person["name"], person["age"])

        if person.get("wife"):
            new_person.wife = person["wife"]
        elif person.get("husband"):
            new_person.husband = person["husband"]

        list_of_people.append(new_person)

    for dude in list_of_people:
        if "wife" in dude.__dict__:
            name = dude.wife
            dude.wife = Person.people[name]
        elif "husband" in dude.__dict__:
            name = dude.husband
            dude.husband = Person.people[name]

    return list_of_people
