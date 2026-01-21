class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(data: list) -> "Person":

    person_list = [Person(person_data["name"], person_data["age"])
                   for person_data in data]

    for person_data in data:
        person = Person.people[person_data["name"]]

        if wife_name := person_data.get("wife"):
            person.wife = Person.people.get(wife_name)

        if husband_name := person_data.get("husband"):
            person.husband = Person.people.get(husband_name)

    return person_list
