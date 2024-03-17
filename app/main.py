class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def take_person_from_list(name: str, people_list: list[Person]) -> Person:
    for person in people_list:
        if name == person.name:
            return person


def create_person_list(people: list[dict]) -> list[Person]:
    people_list = [
        Person(person["name"], person["age"])
        for person in people
    ]

    for person in people:
        if person.get("wife") and person["wife"]:
            wife = take_person_from_list(person["wife"], people_list)
            husband = take_person_from_list(person["name"], people_list)

            wife.husband, husband.wife = husband, wife

    return people_list
