class Person:
    people = {}  # атрибут класу — реєстр усіх створених Person за іменем

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[name] = self  # реєструємо себе одразу при створенні


def create_person_list(people):
    result = []

    # Перший прохід: створюємо всі об'єкти Person (без wife/husband)
    for person_dict in people:
        new_person = Person(person_dict["name"], person_dict["age"])
        result.append(new_person)

    # Другий прохід: додаємо посилання на wife/husband, коли всі об'єкти вже створені
    for person_dict, person_instance in zip(people, result):
        if "wife" in person_dict and person_dict["wife"] is not None:
            person_instance.wife = Person.people[person_dict["wife"]]
        elif "husband" in person_dict and person_dict["husband"] is not None:
            person_instance.husband = Person.people[person_dict["husband"]]

    return result