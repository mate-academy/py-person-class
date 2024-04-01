class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list["Person"]) -> list:
    result = []

    for person in people:
        person_info = Person(person["name"], person["age"])
        result.append(person_info)

        if "wife" in person and person["wife"]:
            wife_name = person["wife"]
            wife = Person.people.get(wife_name)
            if wife:
                setattr(person_info, "wife", wife)
                setattr(wife, "husband", person_info)

    return result
