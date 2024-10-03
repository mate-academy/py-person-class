class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_data: list) -> list:
    person_list = [
        Person(data.get("name"), data.get("age"))
        for data in people_data
        if data.get("name")
    ]

    for data in people_data:
        name = data.get("name")
        if name in Person.people:
            person = Person.people[name]
            wife_name = data.get("wife")
            husband_name = data.get("husband")

            if wife_name:
                person.wife = Person.people.get(wife_name)
            if husband_name:
                person.husband = Person.people.get(husband_name)

    return person_list
