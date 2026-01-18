class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:

        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]

    for i in people:
        spouse_name = i.get("wife") or i.get("husband")
        if spouse_name:
            person = Person.people[i["name"]]
            spouse = Person.people[spouse_name]
            setattr(person, "wife" if i.get("wife") else "husband", spouse)

    return person_list
