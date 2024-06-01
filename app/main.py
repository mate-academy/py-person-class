
class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

    def __repr__(self) -> str:
        spouse = ""
        if hasattr(self, "wife"):
            spouse = f", wife={self.wife.name}"
        if hasattr(self, "husband"):
            spouse = f", husband={self.husband.name}"
        return f"Person(name={self.name}, age={self.age}{spouse})"


def create_person_list(people: list) -> list:
    person_list = []
    for person_dict in people:
        name = person_dict["name"]
        age_str = person_dict["age"]
        if name is None or age_str is None:
            raise ValueError("Name and age must be provided")

        try:
            age = int(age_str)
        except ValueError:
            raise ValueError(f"Age must be an integer, got {age_str}")
        person_list.append(Person(name, age))

    for person_dict in people:
        name = person_dict["name"]
        person_spouse = Person.people[name]
        if "wife" in person_dict and person_dict["wife"] is not None:
            if person_dict["wife"] in Person.people:
                person_spouse.wife = Person.people[person_dict["wife"]]
        if "husband" in person_dict and person_dict["husband"] is not None:
            if person_dict["husband"] in Person.people:
                person_spouse.husband = Person.people[person_dict["husband"]]

    return person_list
