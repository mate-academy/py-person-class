class Person:
    # Атрибут класу для зберігання всіх створених екземплярів
    people = {}

    def __init__(self, name: str, age: int) -> None:
        """
        Ініціалізує обєкт класу Person.

        :param name: Імя людини (string).
        :param age: Вік людини (int).
        """
        self.name = name
        self.age = age
        # Додаємо новий екземпляр у словник класу
        Person.people[name] = self


def create_person_list(people: list) -> None:
    """
    Створює список екземплярів класу
    Person на основі вхідного списку словників.
    :param people: Список словників, де кожен словник описує людину.
    :return: Список екземплярів класу Person.
    """
    # Створюємо екземпляри класу Person
    for person_data in people:
        Person(person_data["name"], person_data["age"])

    # Встановлюємо звязки wife/husband
    for person_data in people:
        person = Person.people[person_data["name"]]
        if "wife" in person_data and person_data["wife"] is not None:
            person.wife = Person.people[person_data["wife"]]
        if "husband" in person_data and person_data["husband"] is not None:
            person.husband = Person.people[person_data["husband"]]

    # Повертаємо список екземплярів класу
    return list(Person.people.values())
