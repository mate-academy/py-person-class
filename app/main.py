class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people_data: list) -> list:
    people = []

    for person_dict in people_data:
        name = person_dict.get("name")
        age = person_dict.get("age")

        person = Person(name, age)
        people.append(person)

    for person_dict in people_data:
        person = people[people_data.index(person_dict)]

        if person_dict.get("wife") is not None:
            wife_name = person_dict.get("wife")

            if wife_name in Person.people:
                person.wife = Person.people[wife_name]
                Person.people[wife_name].husband = person

        if person_dict.get("husband") is not None:
            husband_name = person_dict.get("husband")

            if husband_name in Person.people:
                person.husband = Person.people[husband_name]
                Person.people[husband_name].wife = person

    return people
