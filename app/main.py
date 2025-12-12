from typing import List, Dict, Any, Optional


class Person:
    """
    Клас, що представляє особу. Зберігає всі створені екземпляри 
    у атрибуті класу 'people'.
    """
    # Атрибут класу: Словник для зберігання всіх екземплярів Person
    people: Dict[str, 'Person'] = {}

    def __init__(self, name: str, age: int) -> None:
        """
        Конструктор, що ініціалізує ім'я та вік, та додає екземпляр у Person.people.
        """
        self.name = name
        self.age = age
        # Додавання поточного екземпляра до словника класу
        Person.people[name] = self

    # Допоміжний метод для зручного відображення об'єкта
    def __repr__(self) -> str:
        partner_obj = getattr(self, 'wife', None) or getattr(self, 'husband', None)
        partner_name = partner_obj.name if partner_obj else "None"
        return f"Person(name='{self.name}', age={self.age}, partner='{partner_name}')"


def create_person_list(people_dicts: List[Dict[str, Any]]) -> List[Person]:
    """
    Перетворює список словників на список екземплярів Person та 
    встановлює зв'язки партнерства.
    """
    # Скидаємо словник people, щоб обробляти лише поточну партію даних
    Person.people = {}

    # 1. Створення всіх об'єктів Person (Попкляє Person.people через __init__)
    # Використовуємо list comprehension для створення екземплярів
    person_list = [
        Person(person_data["name"], person_data["age"])
        for person_data in people_dicts
    ]

    # 2. Встановлення зв'язків (Потрібні всі об'єкти в кеші)
    for person_data in people_dicts:
        # Отримуємо об'єкт по імені з кешу класу
        person_obj = Person.people[person_data["name"]]

        # Встановлення атрибута 'wife'
        if "wife" in person_data and person_data["wife"] is not None:
            partner_name = person_data["wife"]
            # Посилання на об'єкт партнера (Rachel)
            person_obj.wife = Person.people[partner_name]

        # Встановлення атрибута 'husband'
        if "husband" in person_data and person_data["husband"] is not None:
            partner_name = person_data["husband"]
            # Посилання на об'єкт партнера (Ross)
            person_obj.husband = Person.people[partner_name]

    # 3. Повертаємо результат після завершення всіх зв'язків
    return person_list