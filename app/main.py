class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self  # Add the person to the people dictionary

    def __repr__(self) -> str:
        return f"Person(name={self.name}, age={self.age})"


def create_person_list(people: list) -> list:
    person_list = []

    for person_data in people:
        person_instance = Person(name=person_data["name"],
                                 age=person_data["age"])
        person_list.append(person_instance)

    for person_data in people:
        person_instance = Person.people[person_data["name"]]
        if "wife" in person_data and person_data["wife"]:
            person_instance.wife = Person.people[person_data["wife"]]
        if "husband" in person_data and person_data["husband"]:
            person_instance.husband = Person.people[person_data["husband"]]

    return person_list
