class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        Person.people[name] = self

    def set_spouse(self, spouse_name: str) -> None:
        if not spouse_name:  # Перевірка на None або порожній рядок
            return
        spouse = Person.people.get(spouse_name)
        if spouse:
            if self.age % 2 == 0:
                self.wife = spouse
                spouse.husband = self
            else:
                self.husband = spouse
                spouse.wife = self

    def remove_spouse(self) -> None:
        # Видалення атрибутів тільки якщо вони не потрібні
        if self.wife is None:
            del self.wife
        if self.husband is None:
            del self.husband


def create_person_list(people: list) -> list:
    return [
        (person := Person(person_data["name"], person_data["age"]))
        .set_spouse(person_data.get("wife") or person_data.get("husband"))
        or person.remove_spouse()
        or person
        for person_data in people
    ]
