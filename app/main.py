class Person:

    people = {}

    def __init__(self, name: str, age: int) -> any:
        self.name = name
        self.age = age
        Person.people[name] = self

    def set_spouse(self, spouse_name: str, spouse_role: str) -> None:
        spouse = Person.people.get(spouse_name)
        if spouse:
            setattr(self, spouse_role, spouse)


def create_person_list(people: list) -> list:

    person_list = []

    for person_data in people:
        person = Person(name=person_data["name"], age=person_data["age"])
        person_list.append(person)

    for person_data in people:
        person = Person.people[person_data["name"]]
        if "wife" in person_data and person_data["wife"] is not None:
            person.set_spouse(person_data["wife"], "wife")
        elif "husband" in person_data and person_data["husband"] is not None:
            person.set_spouse(person_data["husband"], "husband")

    return person_list
