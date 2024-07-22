class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for person_data in people:
        person_list.append(Person(name=person_data["name"], age=person_data["age"]))

    for person_data, person in zip(people, person_list):
        if "wife" in person_data and person_data["wife"] is not None:
            wife_name = person_data["wife"]
            wife_person = Person.people.get(wife_name, None)
            if wife_person:
                person.wife = wife_person
                wife_person.husband = person

        if "husband" in person_data and person_data["husband"] is not None:
            husband_name = person_data["husband"]
            husband_person = Person.people.get(husband_name, None)
            if husband_person:
                person.husband = husband_person
                husband_person.wife = person

    return person_list
