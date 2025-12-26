class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None

        Person.people[name] = self


def create_person_list(people_list: list) -> list:
    persons = []

    for one in people_list:
        name = one["name"]
        age = one["age"]
        person = Person(name, age)
        persons.append(person)

    for one in people_list:
        name = one["name"]
        person = Person.people[name]

        if "wife" in one and one["wife"]:
            person.wife = Person.people.get(one["wife"])
        elif "husband" in one and one["husband"]:
            person.husband = Person.people.get(one["husband"])

    return persons
