class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

    def set_spouse(
            self, spouse_name: str, is_wife: bool = True
    ) -> None:
        spouse = Person.people[spouse_name]

        if is_wife:
            # setattr to bypass static type linter warnings
            setattr(self, "wife", spouse)
            spouse.husband = self
        else:
            setattr(self, "husband", spouse)
            spouse.wife = self


def create_person_list(people: list) -> list:
    for person in people:

        new_person = Person(name=person["name"], age=person["age"])

        if person.get("wife") in Person.people.keys():
            new_person.set_spouse(
                spouse_name=person["wife"],
                is_wife=True
            )

        if person.get("husband") in Person.people.keys():
            new_person.set_spouse(
                spouse_name=person["husband"],
                is_wife=False
            )

    return list(Person.people.values())
