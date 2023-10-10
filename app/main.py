class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person_data in people:
        name = person_data.get("name")
        age = person_data.get("age")
        person = Person(name, age)

        if "wife" in person_data and person_data["wife"] is not None:
            wife_name = person_data["wife"]
            wife = Person.people.get(wife_name)
            if wife:
                person.wife = wife
                wife.husband = person

        if "husband" in person_data and person_data["husband"] is not None:
            husband_name = person_data["husband"]
            husband = Person.people.get(husband_name)
            if husband:
                person.husband = husband
                husband.wife = person

        person_list.append(person)

    return person_list
