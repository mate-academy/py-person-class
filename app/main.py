class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        self.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person_data in people:
        name = person_data["name"]
        age = person_data["age"]

        person = Person(name, age)

        if "wife" in person_data and person_data["wife"] in Person.people:
            person.wife = Person.people[person_data["wife"]]
            person.wife.husband = person

        elif "husband" in person_data and person_data["husband"] in Person.people:
            person.husband = Person.people[person_data["husband"]]
            person.husband.wife = person

        person_list.append(person)

    return person_list