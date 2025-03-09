class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        if name not in Person.people:
            Person.people[name] = self

            # self.wife = None
            # self.husband = None

    def __repr__(self) -> str:
        spouse = getattr(self, "wife", None) or getattr(self, "husband", None)
        spouse_str = f", spouse={spouse.name}" if spouse else ""
        return f"Person(name={self.name}, age={self.age}{spouse_str})"


def create_person_list(people_list: list) -> list:
    for person_data in people_list:
        if person_data["name"] not in Person.people:
            Person(person_data["name"], person_data["age"])

    for person_data in people_list:
        person = Person.people[person_data["name"]]

        if "wife" in person_data and person_data["wife"]:
            setattr(person, "wife", Person.people.get(person_data["wife"]))

        if "husband" in person_data and person_data["husband"]:
            setattr(person, "husband",
                    Person.people.get(person_data["husband"]))

    return [Person.people[person_data["name"]] for person_data in people_list]
