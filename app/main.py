class Person:

    people = {}   # class attribute

    def __init__(self, name: str, age: int) -> None:
        self.name = name  # instance attribute
        self.age = age  # instance attribute
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]
    for person in people:
        new_key = "wife" if "wife" in person else "husband"
        if person.get(new_key) and person.get(new_key) in Person.people.keys():
            setattr(
                Person.people[person["name"]],
                new_key, Person.people[person[new_key]]
            )
    return person_list
