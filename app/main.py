class Person:
    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age

        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    persons_list: list[Person] = []

    for person_dict in people:
        person = Person(person_dict["name"], person_dict["age"])

        persons_list.append(person)

        if "wife" in person_dict:
            person.partner_name: str = person_dict["wife"]
            if person.partner_name is not None:
                person.wife: Person = None
        else:
            person.partner_name: str = person_dict["husband"]
            if person.partner_name is not None:
                person.husband: Person = None

    for person in persons_list:
        if hasattr(person, "wife"):
            person.wife = Person.people[person.partner_name]
        elif hasattr(person, "husband"):
            person.husband = Person.people[person.partner_name]

    return persons_list
