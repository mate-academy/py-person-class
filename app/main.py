class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list[Person]:
    p_list = [Person(person["name"], person["age"]) for person in people]
    for person_data, person in zip(people, p_list):
        if person_data.get("wife"):
            wife = Person.people.get(person_data["wife"])
            if wife:
                person.wife = wife
        elif person_data.get("husband"):
            husband = Person.people.get(person_data["husband"])
            if husband:
                person.husband = husband
    return p_list
