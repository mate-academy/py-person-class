class Person:
    people = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    # Створюємо всіх людей, зберігаючи їх у списку person_list
    for person in people:
        person_to_list = Person(person["name"], person["age"])
        person_list.append(person_to_list)

    # Установлюємо партнерів для кожної людини
    for person in people:
        person_to_spouses = Person.people[person["name"]]
        if person.get("wife"):
            person_to_spouses.wife = Person.people[person["wife"]]
        if person.get("husband"):
            person_to_spouses.husband = Person.people[person["husband"]]

    return person_list
