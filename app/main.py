class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_data: dict) -> list[Person]:
    person_list = []

    for person_item in people_data:
        name = person_item["name"]
        age = person_item["age"]
        person = Person(name, age)

        person_list.append(person)

    for index, person in enumerate(people_data):
        wife = person.get("wife")
        husband = person.get("husband")
        if wife is not None:
            person_list[index].wife = Person.people.get(wife)
        if husband is not None:
            person_list[index].husband = Person.people.get(husband)

    return person_list
