class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [
        Person(one_people["name"], one_people["age"]) for one_people in people
    ]

    for one_people in people:
        if one_people.get("wife") is not None:
            wife_name = one_people.get("wife")
            wife = Person.people[wife_name]
            new_people = Person.people[one_people.get("name")]
            if wife is not None:
                new_people.wife = wife
                wife.husband = new_people
    return person_list
