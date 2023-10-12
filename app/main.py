class Person:
    people = {}

    def __init__(
            self,
            name: str,
            age: int
    ) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for person_date in people:
        name = person_date["name"]
        age = person_date["age"]
        person = Person(name, age)

        if "wife" in person_date:
            wife_name = person_date["wife"]
            if wife_name is not None and wife_name in Person.people:
                person.wife = Person.people[wife_name]
                Person.people[wife_name].husband = person

        if ("husband" in person_date
                and person_date["husband"] is not None):
            husband_name = person_date["husband"]
            if husband_name in Person.people:
                person.husband = Person.people[husband_name]
                Person.people[husband_name].wife = person

        person_list.append(person)

    return person_list
