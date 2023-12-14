class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_data: list) -> list:
    person_list = []
    for person_data in people_data:
        name = person_data["name"]
        age = person_data["age"]
        person = Person(name, age)
        person_list.append(person)
    for person_data in people_data:
        name = person_data["name"]
        wife_name = person_data.get("wife")
        husband_name = person_data.get("husband")
        if wife_name:
            person = Person.people[name]
            wife = Person.people.get(wife_name)
            person.wife = wife
        elif husband_name:
            person = Person.people[name]
            husband = Person.people.get(husband_name)
            person.husband = husband

    return person_list
