class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self

    def __repr__(self) -> str:
        return f"<Person: {self.name}>"


def create_person_list(people: list[dict]) -> list[Person]:
    Person.people.clear()

    # [CHECKLIST ITEM #3] Refactored to list comprehension
    [Person(person_data["name"], person_data["age"]) for person_data in people]

    for person_data in people:
        person_obj = Person.people[person_data["name"]]

        # [CHECKLIST ITEM #4] Use .get() for "wife"
        wife_name = person_data.get("wife")
        if wife_name is not None:
            person_obj.wife = Person.people[wife_name]

        # [CHECKLIST ITEM #4] Use .get() for "husband"
        husband_name = person_data.get("husband")
        if husband_name is not None:
            person_obj.husband = Person.people[husband_name]

    return list(Person.people.values())
