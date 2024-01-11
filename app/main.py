class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people.update({name: self})


def create_person_list(people: list[dict]) -> list[Person]:
    persons_of_people = [
        Person(name=person["name"], age=person["age"])
        for person in people
    ]
    for person, person_info in zip(persons_of_people, people):
        if "wife" in person_info and person_info["wife"] is not None:
            person.wife = Person.people[person_info["wife"]]
        if "husband" in person_info and person_info["husband"] is not None:
            person.husband = Person.people[person_info["husband"]]
    return persons_of_people
