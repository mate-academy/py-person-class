class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = []

    # Сначала создаём всех людей
    for data in people:
        name = data["name"]
        age = data["age"]
        person = Person(name, age)
        result.append(person)

    # Теперь создаём связи husband/wife
    for data in people:
        person = Person.people[data["name"]]

        if "wife" in data and data["wife"] is not None:
            wife = Person.people.get(data["wife"])
            setattr(person, "wife", wife)
            setattr(wife, "husband", person)

        if "husband" in data and data["husband"] is not None:
            husband = Person.people.get(data["husband"])
            setattr(person, "husband", husband)
            setattr(husband, "wife", person)

    return result
