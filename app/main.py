class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    list_people = []
    for person_value in people:
        name = person_value["name"]
        age = person_value["age"]
        person = Person(name, age)
        list_people.append(person)

    for person_data in people:
        person = Person.people.get(person_data["name"])
        wife_name = person_data.get("wife")
        husband_name = person_data.get("husband")

        if wife_name is not None:
            person.wife = Person.people.get(wife_name)

        if husband_name is not None:
            person.husband = Person.people.get(husband_name)

    return list_people
