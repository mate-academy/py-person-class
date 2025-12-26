class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    # 💡 Critical fix: очищення спільного стану
    Person.people.clear()

    # 1️⃣ Створюємо всіх людей (list comprehension — краща практика)
    [Person(entry["name"], entry["age"]) for entry in people]

    # 2️⃣ Встановлюємо зв’язки
    for entry in people:
        person = Person.people[entry["name"]]

        # Отримуємо імена подружжя без помилок, навіть якщо ключів нема
        wife_name = entry.get("wife")
        husband_name = entry.get("husband")

        # Якщо є дружина
        if wife_name:
            spouse = Person.people.get(wife_name)
            if spouse:
                person.wife = spouse
                spouse.husband = person

        # Якщо є чоловік
        if husband_name:
            spouse = Person.people.get(husband_name)
            if spouse:
                person.husband = spouse
                spouse.wife = person

    # 3️⃣ Повертаємо список осіб у тому ж порядку, що й у вхідних даних
    return [Person.people[entry["name"]] for entry in people]
