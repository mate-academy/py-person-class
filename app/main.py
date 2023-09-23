class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        if name not in Person.people:
            self.name = name
            self.age = age

            Person.people[self.name] = self

    def set_spouse(self, key: str, spouse: "Person") -> None:
        if key == "wife":
            self.wife = spouse
        elif key == "husband":
            self.husband = spouse


def create_person_list(people: list) -> list:
    for person in people:
        Person(person["name"], person["age"])

    # when persons exist, relations can be created without checking existence
    for person in people:
        key, spouse_name = list(person.items())[2]
        if spouse_name is not None:
            spouse = Person.people[spouse_name]
            Person.people[person["name"]].set_spouse(key, spouse)

    return list(Person.people.values())
