class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    """
    Приймає список словників (людей),
    створює екземпляри Person і повертає список цих об"єктів.
    Якщо у словнику вказано "wife" або "husband",
    створює відповідне посилання між об"єктами.
    """

    person_list = [Person(d["name"], d["age"]) for d in people]

    for person_dict in people:
        person = Person.people[person_dict["name"]]

        for role in ("wife", "husband"):
            partner_name = person_dict.get(role)
            if partner_name:
                setattr(person, role, Person.people[partner_name])

    return person_list
