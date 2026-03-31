class Person:
    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_data: list) -> list:
    Person.people.clear()

    instances = [Person(data.get("name"),
                        data.get("age")) for data in people_data]

    for data in people_data:
        name = data.get("name")
        current_person = Person.people.get(name)

        wife_name = data.get("wife")
        if wife_name is not None:
            current_person.wife = Person.people.get(wife_name)

        husband_name = data.get("husband")
        if husband_name is not None:
            current_person.husband = Person.people.get(husband_name)

    return instances
