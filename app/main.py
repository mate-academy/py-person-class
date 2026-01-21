class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_data: list[dict]) -> list[Person]:
    person_instances = []

    # Создаем экземпляры Person для всех людей
    for person_data in people_data:
        person = Person(person_data["name"], person_data["age"])
        person_instances.append(person)

    # Устанавливаем ссылки на wife/husband
    for person_data in people_data:
        person = Person.people[person_data["name"]]
        if "wife" in person_data and person_data["wife"]:
            person.wife = Person.people[person_data["wife"]]
        elif "husband" in person_data and person_data["husband"]:
            person.husband = Person.people[person_data["husband"]]

    return person_instances
