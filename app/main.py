class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person_data in people:
        name = person_data["name"]
        age = person_data["age"]
        person = Person(name, age)

        if "wife" in person_data and person_data["wife"] is not None:
            wife_name = person_data["wife"]
            if wife_name in person.people:  # Використовуємо атрибут екземпляру
                person.wife = person.people[wife_name]
                if person.wife.husband is None:
                    person.wife.husband = person

        elif "husband" in person_data and person_data["husband"] is not None:
            husband_name = person_data["husband"]
            if husband_name in person.people:  # Використовуємо атрибут екземпляру
                person.husband = person.people[husband_name]
                if person.husband.wife is None:
                    person.husband.wife = person

        person_list.append(person)
    return person_list
