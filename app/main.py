class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for person_data in people:
        name = person_data.get("name")
        age = person_data.get("age")

        person = Person(name, age)
        person_list.append(person)

    for person_data in people:
        current_person = Person.people.get(person_data["name"], None)
        current_wife = person_data.get("wife", None)
        if current_wife:
            current_person.wife = Person.people[current_wife]

        current_husband = person_data.get("husband", None)
        if current_husband:
            current_person.husband = Person.people[current_husband]

    return person_list
