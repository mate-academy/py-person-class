class Person:
    people = {}  # Атрибут класса для хранения экземпляров по их имени

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self  # Добавление экземпляра в словарь people


def create_person_list(people_data: list) -> list:

    person_list = []

    # Первый проход: Создание экземпляров Person
    for person_dict in people_data:
        name = person_dict["name"]
        age = person_dict["age"]
        person = Person(name, age)
        person_list.append(person)

    # Второй проход: Назначение ссылок на супругов
    for person_dict, person in zip(people_data, person_list):
        spouse_name = person_dict.get("wife") or person_dict.get("husband")
        if spouse_name:
            spouse = Person.people.get(spouse_name)
            if spouse:
                if "wife" in person_dict:
                    person.wife = spouse
                else:
                    person.husband = spouse

    return person_list
