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
    person_list = [
        Person(person_dict["name"], int(person_dict["age"]))
        for person_dict in people
        if person_dict["name"] is not None and person_dict["age"] is not None
    ]

    for person_dict in people:
        name = person_dict["name"]
        person_spouse = Person.people[name]
        wife_name = person_dict.get("wife")
        if wife_name is not None and wife_name in Person.people:
            person_spouse.wife = Person.people[wife_name]
        husband_name = person_dict.get("husband")
        if husband_name is not None and husband_name in Person.people:
            person_spouse.husband = Person.people[husband_name]

    return person_list
