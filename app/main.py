class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_data: list[dict]) -> list[Person]:
    instances = [
        Person(data["name"], data["age"])
        for data in people_data
    ]

    for data in people_data:
        person_instance = Person.people[data["name"]]
        husband_name = data.get("husband")
        wife_name = data.get("wife")

        if husband_name:
            person_instance.husband = Person.people.get(husband_name)
        if wife_name:
            person_instance.wife = Person.people.get(wife_name)

    return instances
