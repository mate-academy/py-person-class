class Person:
    # Атрибут класу, який буде зберігати екземпляри класу за їхніми іменами
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        # Додаємо екземпляр до класового атрибуту people
        Person.people[name] = self


def create_person_list(people: list) -> list:
    # Створюю порожній список для зберігання екземплярів Person
    person_instances = []

    # Спочатку створюємо всі екземпляри Person
    for person in people:
        # Отримую (витягую) значення "name" та "age" зі словника є
        name = person["name"]
        age = person["age"]
        # Створення екземпляру Person
        person_instance = Person(name, age)
        person_instances.append(person_instance)

    # Потім встановлюємо звʼязки між чоловіком і дружиною
    for person in people:
        person_instance = Person.people[person["name"]]

        wife = person.get("wife")
        husband = person.get("husband")

        # Встановлення звʼязків між людьми
        if wife:
            person_instance.wife = Person.people.get(wife)
            # Також встановлюємо, що дружина має чоловіка
            Person.people[wife].husband = person_instances

        if husband:
            person_instance.husband = Person.people.get(husband)
            # Також встановлюємо, що чоловік має дружину
            Person.people[husband].wife = person_instance

    return person_instances
