class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [
        Person(person_dict["name"], person_dict["age"])
        for person_dict in people
    ]
    for person_dict in people:
        name = person_dict["name"]
        person = Person.people[name]

        wife_name = person_dict.get("wife")
        husband_name = person_dict.get("husband")

        if wife_name:
            person.wife = Person.people.get(wife_name)
        if husband_name:
            person.husband = Person.people.get(husband_name)

    return person_list
