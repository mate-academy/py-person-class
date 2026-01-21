class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(
        people_list: list[dict[str, str | int | None]]
) -> list[Person]:
    person_objects = []

    for person in people_list:
        person_objects.append(Person(person["name"], person["age"]))

    # Встановлюємо посилання на чоловіка/дружину
    for person in people_list:
        person_instance = Person.people[person["name"]]
        if "wife" in person and person["wife"] is not None:
            setattr(
                person_instance, "wife",
                Person.people.get(person["wife"]))
        if "husband" in person and person["husband"] is not None:
            setattr(
                person_instance, "husband",
                Person.people.get(person["husband"]))

    return person_objects
