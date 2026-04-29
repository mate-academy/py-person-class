class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]

    for person_data in people:
        husband_name = person_data.get("husband")
        wife_name = person_data.get("wife")
        person = Person.people[person_data["name"]]

        if wife_name and (spouse := Person.people.get(wife_name)):
            person.wife = spouse
        elif husband_name and (spouse := Person.people.get(husband_name)):
            person.husband = spouse

    return person_list
