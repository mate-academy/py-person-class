class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    list_of_people = [
        Person(person_data["name"], person_data["age"])
        for person_data in people
    ]

    for person_data in people:
        person = Person.people[person_data["name"]]

        wife = Person.people.get(person_data.get("wife"))
        if wife is not None:
            person.wife = wife
            wife.husband = person

        husband = Person.people.get(person_data.get("husband"))
        if husband is not None:
            person.husband = husband
            husband.wife = person

    return list_of_people
