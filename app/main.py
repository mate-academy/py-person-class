class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = [Person(subject["name"], subject["age"]) for subject in people]

    for subject in people:
        if subject.get("wife") is not None:
            current_person = Person.people[subject["name"]]
            current_person.wife = Person.people[subject["wife"]]
        elif subject.get("husband") is not None:
            current_person = Person.people[subject["name"]]
            current_person.husband = Person.people[subject["husband"]]

    return result


if __name__ == "__main__":
    people = [
        {"name": "Ross", "age": 30, "wife": "Rachel"},
        {"name": "Joey", "age": 29, "wife": None},
        {"name": "Rachel", "age": 28, "husband": "Ross"}
    ]

    person_list = create_person_list(people)
