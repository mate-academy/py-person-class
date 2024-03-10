class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    # Получаем экземпляр класса Person по имени из атрибута people
    for person_data in people:
        Person(person_data["name"], person_data["age"])
    # Проверка информация о супруге в словаре people
    for person_data in people:
        person_instance = Person.people.get(person_data["name"])
        wife_name = person_data.get("wife")
        husband_name = person_data.get("husband")
        # Установка атрибута wife объекта Person на другой объкт
        if wife_name in Person.people:
            person_instance.wife = Person.people[wife_name]
        # Установка атрибута husband объекта Person на другой объкт
        if husband_name in Person.people:
            person_instance.husband = Person.people[husband_name]
    return list(Person.people.values())
