class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        if name in Person.people:
            print(f"Error: A person with the name \"{name}\" already exists.")
        else:
            self.name = name
            self.age = age
            Person.people[name] = self


def create_person_list(people: list) -> list:
    persons = []

    for person_data in people:
        name = person_data["name"]
        age = person_data["age"]
        if name not in Person.people:
            person = Person(name, age)
            persons.append(person)
        else:
            persons.append(Person.people[name])  # Використати вже створеного

    # Додавання атрибутів wife та husband
    for person_data in people:
        person = Person.people[person_data["name"]]

        # Перевірка існування дружини
        if "wife" in person_data and person_data["wife"]:
            wife_name = person_data["wife"]
            if wife_name in Person.people:
                person.wife = Person.people[wife_name]
            else:
                print(f"Warning: Wife with name \"{wife_name}\" don't exist")

        # Перевірка існування чоловіка
        if "husband" in person_data and person_data["husband"]:
            husband_name = person_data["husband"]
            if husband_name in Person.people:
                person.husband = Person.people[husband_name]
            else:
                print(f"Husband with name \"{husband_name}\" don't exist")

    return persons
