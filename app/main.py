class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def add_person(self, person: "Person") -> None:
        if person.name not in Person.people:
            Person.people[person.name] = person


def create_person_list(people: list) -> list:
    result = [
        Person(person["name"], person["age"]) for person in people
    ]

    for person, person_data in zip(result, people):
        if person_data.get("wife"):
            person.wife_name = person_data["wife"]
        if person_data.get("husband"):
            person.husband_name = person_data["husband"]
        person.add_person(person)

    for item in result:
        if hasattr(item, "wife_name"):
            for item2 in result:
                if hasattr(item2, "husband_name"):
                    if item.name == item2.husband_name:
                        item.wife = item2
                        item2.husband = item

    return result
