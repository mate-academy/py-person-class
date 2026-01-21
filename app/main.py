class Person:
    people = {}  # Класс-атрибут для хранения всех экземпляров по имени

    def __init__(self, name: str, age: int) -> None :
        self.name = name
        self.age = age
        Person.people[name] = self  # Добавляем экземпляр в словарь


def create_person_list(people_data: dict) -> list:
    Person.people.clear()
    # Шаг 1: создаём все экземпляры Person без связей
    for data in people_data:
        Person(name=data["name"], age=data["age"])

    # Шаг 2: устанавливаем wife/husband ссылки
    for data in people_data:
        person = Person.people[data["name"]]
        if "wife" in data and data["wife"]:
            person.wife = Person.people.get(data["wife"])
        if "husband" in data and data["husband"]:
            person.husband = Person.people.get(data["husband"])

    # Возвращаем список всех созданных экземпляров
    return list(Person.people.values())
