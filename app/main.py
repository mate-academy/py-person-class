class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    person_list = []
    for person_dict in people:
        person = Person(person_dict["name"], person_dict["age"])
        person_list.append(person)

    for person, person_dict in zip(person_list, people):
        if "wife" in person_dict and person_dict["wife"] is not None:
            wife = Person.people.get(person_dict["wife"])
            if wife:
                person.wife = wife
                wife.husband = person
        if "husband" in person_dict and person_dict["husband"] is not None:
            husband = Person.people.get(person_dict["husband"])
            if husband:
                person.husband = husband
                husband.wife = person

    return person_list
