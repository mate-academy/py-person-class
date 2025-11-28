class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

    def __repr__(self) -> str:
        return f"Person(name={self.name}, age={self.age})"


def create_person_list(people: list) -> list:
    Person.people = {}
    person_list = []

    for person in people:
        p = Person(person["name"], person["age"])
        person_list.append(p)

    for data in people:
        name = data["name"]
        instance = Person.people[name]

        wife_name = data.get("wife")
        if wife_name is not None and wife_name in Person.people:
            instance.wife = Person.people[wife_name]

        husband_name = data.get("husband")
        if husband_name is not None and husband_name in Person.people:
            instance.husband = Person.people[husband_name]

    return person_list