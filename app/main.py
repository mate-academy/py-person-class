class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

    def set_spouse(self, spouse_name: str, is_husband: bool) -> None:
        if spouse_name in Person.people:
            spouse = Person.people[spouse_name]
            if is_husband:
                self.wife = spouse
                spouse.husband = self
            else:
                self.husband = spouse
                spouse.wife = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]

    for person_dict, person in zip(people, person_list):
        if "wife" in person_dict and person_dict["wife"]:
            person.set_spouse(person_dict["wife"], is_husband=True)
        elif "husband" in person_dict and person_dict["husband"]:
            person.set_spouse(person_dict["husband"], is_husband=False)

    return person_list
