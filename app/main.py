class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    # створюємо всіх людей через list comprehension
    result = [Person(p["name"], p["age"]) for p in people]

    # встановлюємо зв’язки
    for person in people:
        wife = person.get("wife")
        if wife:
            Person.people[person["name"]].wife = Person.people[wife]

        husband = person.get("husband")
        if husband:
            Person.people[person["name"]].husband = Person.people[husband]

    return result
