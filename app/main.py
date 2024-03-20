class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person_data in people:
        person = Person(person_data["name"], person_data["age"])
        if "wife" in person_data and person_data["wife"]:
            person.wife = Person.people.get(person_data["wife"])
        elif "husband" in person_data and person_data["husband"]:
            person.husband = Person.people.get(person_data["husband"])
            if person.husband:
                person.husband.wife = person
        person_list.append(person)
    return person_list
