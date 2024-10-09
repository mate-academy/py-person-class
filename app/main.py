class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list[dict[str, str | int]]) -> list[Person]:
    person_list: list[Person] = [
        Person(
            name=person_dict["name"],
            age=person_dict["age"]
        )
        for person_dict in people
    ]

    for person_dict in people:
        person = Person.people[person_dict["name"]]
        if "wife" in person_dict and person_dict["wife"] is not None:
            person.wife = Person.people[person_dict["wife"]]
        elif hasattr(person, "wife"):  # Перевіряємо атрибут wife
            delattr(person, "wife")  # Видаляємо атрибут, якщо його немає

        if "husband" in person_dict and person_dict["husband"] is not None:
            person.husband = Person.people[person_dict["husband"]]
        elif hasattr(person, "husband"):  # Перевіряємо атрибут husband
            delattr(person, "husband")  # Видаляємо атрибут, якщо його немає

    return person_list
