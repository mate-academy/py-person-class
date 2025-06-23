class Person:
    people = {}  # Класовий атрибут: name -> екземпляр

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        # Додаємо цю особу до словника people
        Person.people[name] = self


def create_person_list(people: list) -> list:
    # створюємо список всіх Person без дружина/чоловік
    person_list = []
    for person_data in people:
        name = person_data["name"]
        age = person_data["age"]
        person = Person(name, age)
        person_list.append(person)

    # встановлюємо дружина/чоловік
    for person_data in people:
        name = person_data["name"]
        person = Person.people[name]

        if person_data.get("wife"):
            person.wife = Person.people[person_data["wife"]]
        elif person_data.get("husband"):
            person.husband = Person.people[person_data["husband"]]

    return person_list
