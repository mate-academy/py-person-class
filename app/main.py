class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

    def __repr__(self) -> str:
        return f"Person({self.name}, {self.age})"


def create_person_list(people: list) -> list:

    person_list = [Person(person["name"], person["age"]) for person in people]

    for person_data in people:
        person = Person.people[person_data["name"]]

        wife = person_data.get("wife")
        if "wife" in person_data and wife is not None:
            person.wife = Person.people[wife]

        husband = person_data.get("husband")
        if "husband" in person_data and husband is not None:
            person.husband = Person.people[husband]

    return person_list
