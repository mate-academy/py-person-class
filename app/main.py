class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons = []
    for current_people in people:
        name = current_people["name"]
        age = current_people["age"]
        person = Person(name, age)
        if current_people.get("wife") is not None:
            person.wife = Person.people[name]
            Person.people[name].husband = person
        if current_people.get("husband") is not None:
            person.husband = Person.people[name]
            Person.people[name].wife = person

        persons.append(person)

    return persons
