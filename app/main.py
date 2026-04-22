class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = []
    for person in people:
        name = person["name"]
        age = person["age"]
        person_instance = Person(name, age)
        result.append(person_instance)
    for i in range(len(people)):
        data = people[i]
        person_instance = result[i]

        if "wife" in data and data["wife"] is not None:
            person_instance.wife = Person.people[data["wife"]]

        # Перевірка на чоловіка
        if "husband" in data and data["husband"] is not None:
            person_instance.husband = Person.people[data["husband"]]

    return result
