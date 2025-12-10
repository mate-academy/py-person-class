class Person:
    # класовий атрибут для зберігання всіх створених екземплярів
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        # додаємо екземпляр у словник класу
        Person.people[name] = self


def create_person_list(people: list[dict[str, object]]) -> list[Person]:
    # спочатку створюємо всі Person без зв’язків
    person_list = [Person(p["name"], p["age"]) for p in people]

    # тепер додаємо зв’язки wife/husband
    for p in people:
        person_instance = Person.people[p["name"]]
        if "wife" in p and p["wife"] is not None:
            person_instance.wife = Person.people[p["wife"]]
        if "husband" in p and p["husband"] is not None:
            person_instance.husband = Person.people[p["husband"]]

    return person_list
