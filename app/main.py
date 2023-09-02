class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    result = []

    for person_data in people:
        person = Person(person_data["name"], person_data["age"])
        result.append(person)

        if "wife" in person_data and person_data["wife"]:
            person.wife = Person.people[person_data["name"]]
            Person.people[person_data["name"]].husband = person
        if "husband" in person_data and person_data["husband"]:
            person.husband = Person.people[person_data["name"]]
            Person.people[person_data["name"]].wife = person

    return result
