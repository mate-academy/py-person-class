class Person:
    # Класс-атрибут: хранит все созданные объекты по имени
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        # Добавляем объект в словарь по имени
        Person.people[name] = self


def create_person_list(people_dicts: list[dict]) -> list[Person]:
    # 1. Сначала создаём все объекты Person (без связей)
    person_list = [Person(p["name"], p["age"]) for p in people_dicts]

    # 2. Потом устанавливаем связи wife/husband
    for p in people_dicts:
        person_obj = Person.people[p["name"]]

        if "wife" in p and p["wife"] is not None:
            # создаём атрибут wife и связываем с объектом
            person_obj.wife = Person.people[p["wife"]]

        if "husband" in p and p["husband"] is not None:
            # создаём атрибут husband и связываем с объектом
            person_obj.husband = Person.people[p["husband"]]

    return personal_list
