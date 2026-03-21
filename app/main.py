class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    # Спочатку створюємо всі екземпляри (без wife/husband)
    instances = []
    for person_dict in people:
        person = Person(name=person_dict["name"], age=person_dict["age"])
        instances.append(person)

    # Потім додаємо зв'язки (всі об'єкти вже є в Person.people)
    for person_dict, person in zip(people, instances):
        for key in ("wife", "husband"):
            if key in person_dict and person_dict[key] is not None:
                setattr(person, key, Person.people[person_dict[key]])

    return instances