class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

    def __repr__(self) -> str:
        return f"Person(name={self.name}, age={self.age})"


def create_person_list(people: list) -> list:
    persons = []

    for data in people:
        person = Person(data["name"], data["age"])
        persons.append(person)

    for data in people:
        person = Person.people[data["name"]]

        if "wife" in data and data["wife"] is not None:
            wife_name = data["wife"]
            if wife_name in Person.people:
                person.wife = Person.people[wife_name]

        if "husband" in data and data["husband"] is not None:
            husband_name = data["husband"]
            if husband_name in Person.people:
                person.husband = Person.people[husband_name]

    return persons
