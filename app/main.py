class Person:
    people = {}  # Хранилище всех созданных людей

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[name] = self  # Сохраняем объект для ссылок на других людей


def create_person_list(people_data: list) -> list:
    # Создаем объекты Person
    for data in people_data:
        Person(data["name"], data["age"])

    # Устанавливаем связи husband/wife
    for data in people_data:
        person = Person.people[data["name"]]
        if "wife" in data and data["wife"]:
            person.wife = Person.people[data["wife"]]
            Person.people[data["wife"]].husband = person
        if "husband" in data and data["husband"]:
            person.husband = Person.people[data["husband"]]
            Person.people[data["husband"]].wife = person

    return list(Person.people.values())
