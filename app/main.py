class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        Person.people[name] = self

    def __repr__(self) -> str:
        return f"Person(name={self.name}, age={self.age})"


def create_person_list(people: list) -> list:
    persons = [Person(person_dict["name"], person_dict["age"])
               for person_dict in people]

    for person_dict in people:
        person = Person.people[person_dict["name"]]
        if "wife" in person_dict and person_dict["wife"] is not None:
            person.wife = Person.people[person_dict["wife"]]
        elif hasattr(person, "wife"):
            delattr(person, "wife")
        if "husband" in person_dict and person_dict["husband"] is not None:
            person.husband = Person.people[person_dict["husband"]]
        elif hasattr(person, "husband"):
            delattr(person, "husband")

    return persons
