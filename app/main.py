class Person:
    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:

    for person_info in people:
        Person(person_info["name"], person_info["age"])

    for person_info in people:
        person = Person.people[person_info["name"]]
        wife_name = person_info.get("wife")

        if wife_name:
            person.wife = Person.people[wife_name]
            person.wife.husband = person

    return list(Person.people.values())
