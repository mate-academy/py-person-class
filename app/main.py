class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    for person in people:
        Person(person["name"], person["age"])

    for person in people:
        person_instance = Person.people.get(person["name"])
        if not person_instance:
            continue

        wife_name = person.get("wife")
        husband_name = person.get("husband")

        if wife_name:
            wife_instance = Person.people.get(wife_name)
            if wife_instance:
                person_instance.wife = wife_instance
                wife_instance.husband = person_instance
            else:
                person_instance.wife = wife_name

        if husband_name:
            husband_instance = Person.people.get(husband_name)
            if husband_instance:
                person_instance.husband = husband_instance
                husband_instance.wife = person_instance
            else:
                person_instance.husband = husband_name

    return list(Person.people.values())
