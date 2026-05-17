class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        # додаємо екземпляр у словник класу
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    # спочатку створюємо всі Person без зв’язків
    person_list: list[Person] = []
    for person_dict in people:
        person = Person(person_dict["name"], person_dict["age"])
        person_list.append(person)

    # тепер додаємо wife/husband посилання
    for person_dict in people:
        current_person = Person.people[person_dict["name"]]
        if "wife" in person_dict and person_dict["wife"] is not None:
            current_person.wife = Person.people[person_dict["wife"]]
        if "husband" in person_dict and person_dict["husband"] is not None:
            current_person.husband = Person.people[person_dict["husband"]]

    return person_list
