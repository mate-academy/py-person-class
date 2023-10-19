class Person:
    people = {}

    def __init__(
            self,
            name: str,
            age: int
    ) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self

    def __repr__(self) -> str:
        return self.name


def create_person_list(people: list) -> list:
    for person_data in people:
        # new_human = Person(human["name"], human["age"])
        new_person = Person(person_data["name"], person_data["age"])
        if ("husband" in person_data
                and person_data["husband"] in Person.people):
            husband_instance = Person.people[person_data["husband"]]
            new_person.husband = husband_instance
            husband_instance.wife = Person.people[person_data["name"]]
        elif ("wife" in person_data
              and person_data["wife"] in Person.people):
            wife_instance = Person.people[person_data["wife"]]
            new_person.wife = wife_instance
            wife_instance.husband = Person.people[person_data["name"]]
    return list(Person.people.values())
