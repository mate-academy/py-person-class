class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()

    person_list = []

    for person_data in people:
        name = person_data["name"]
        age = person_data["age"]
        person = Person(name, age)
        person_list.append(person)

    for person_data in people:
        name = person_data["name"]
        person = Person.people[name]

        if "wife" in person_data and person_data["wife"]:
            spouse = Person.people.get(person_data["wife"])
            if spouse:
                person.wife = spouse

        if "husband" in person_data and person_data["husband"]:
            spouse = Person.people.get(person_data["husband"])
            if spouse:
                person.husband = spouse

    return person_list
