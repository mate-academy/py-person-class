class Person:
    people = {}

    def __init__(self, name: str, age: int, spouse: dict = None) -> None:
        self.name = name
        self.age = age
        self.spouse = None
        Person.people[name] = self

        if spouse:
            if "wife" in spouse:
                self.spouse = Person.people[spouse["wife"]]
            elif "husband" in spouse:
                self.spouse = Person.people[spouse["husband"]]
            if self.spouse:
                self.spouse.spouse = self


def create_person_list(people: list) -> list:
    person_list = []
    for person_data in people:
        person = Person(person_data["name"],
                        person_data["age"],
                        person_data.get("wife") or person_data.get("husband"))
        person_list.append(person)
    return person_list
