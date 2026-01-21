class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    results = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        wife_name = person.get("wife")
        husband_name = person.get("husband")
        if wife_name or husband_name:
            new_person = next(
                item for item in results if item.name == person["name"]
            )
            if wife_name:
                new_person.wife = next(
                    item for item in results if item.name == person["wife"]
                )
            elif husband_name:
                new_person.husband = next(
                    item for item in results if item.name == person["husband"]
                )

    return results
