class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        Person.people[name] = self

    def set_spouse(self, spouse_name: str, is_wife: bool) -> None:
        spouse = Person.people.get(spouse_name)
        if spouse:
            if is_wife:
                self.wife = spouse
                spouse.husband = self
            else:
                self.husband = spouse
                spouse.wife = self


def create_person_list(people: list[dict[str, str]]) -> list[Person]:
    person_instances = []
    for person_dict in people:
        person = Person(person_dict["name"], person_dict["age"])
        if "wife" in person_dict and person_dict["wife"]:
            person.set_spouse(person_dict["wife"], is_wife=True)
        elif "husband" in person_dict and person_dict["husband"]:
            person.set_spouse(person_dict["husband"], is_wife=False)
        person_instances.append(person)
    return person_instances
