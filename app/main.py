class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self

    def set_spouse(self, spouse_name: str) -> str:

        if spouse_name is None:
            return

        spouse = Person.people.get(spouse_name)
        if spouse:
            if not hasattr(self, "wife") and not hasattr(spouse, "husband"):
                self.wife = spouse
                spouse.husband = self
            elif not hasattr(self, "husband") and not hasattr(spouse, "wife"):
                self.husband = spouse
                spouse.wife = self


def create_person_list(people: list) -> list:
    person_instances = [
        Person(person_data["name"], person_data["age"])
        for person_data in people
    ]

    for person_data in people:
        person = Person.people[person_data["name"]]

        if "wife" in person_data:
            person.set_spouse(person_data["wife"])
        elif "husband" in person_data:
            person.set_spouse(person_data["husband"])

    return person_instances
