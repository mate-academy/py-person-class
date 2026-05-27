class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

    def __repr__(self) -> str:
        return f"Person(name={self.name}, age={self.age})"


def create_person_list(people: list[dict]) -> list[Person]:
    result_list = []

    for person in people:
        new_person = Person(person["name"], person["age"])
        result_list.append(new_person)

    for person, new_person in zip(people, result_list):
        if person.get("wife"):
            new_person.wife = Person.people[person["wife"]]
        elif person.get("husband"):
            new_person.husband = Person.people[person["husband"]]

    return result_list
