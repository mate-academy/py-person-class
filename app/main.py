class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]
    for person in person_list:
        spouse = None
        person_key = next(p for p in people if p["name"] == person.name)
        if person_key.get("wife") or person_key.get("husband"):
            spouse = (person_key.get("wife") if "wife" in person_key
                      else person_key.get("husband"))
            spouse_key = "wife" if "wife" in person_key else "husband"
        if spouse:
            spouse_info = next(
                (partner for partner in person_list if partner.name == spouse),
                None)
            if spouse_key == "wife":
                person.wife = spouse_info
                person.wife.husband = person
            else:
                person.husband = spouse_info
                person.husband.wife = person
    return person_list
