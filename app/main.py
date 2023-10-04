class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people_data: dict) -> list[Person]:

    person_list = [Person(person_item["name"], person_item["age"]) for person_item in people_data]

    for index, person in enumerate(people_data):
        wife = person.get("wife")
        husband = person.get("husband")
        if wife:
            person_list[index].wife = Person.people.get(wife)
        if husband:
            person_list[index].husband = Person.people.get(husband)

    return person_list
