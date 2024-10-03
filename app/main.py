class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.gender = None
        self.spouse = None
        Person.people[name] = self

    def assign_gender(self, gender: str) -> None:
        self.gender = gender

    def set_spouse(self, spouse_name: str) -> None:
        if spouse_name in Person.people:
            self.spouse = Person.people[spouse_name]
            self.spouse.spouse = self


def create_person_list(people_data: list) -> list:
    person_list = []

    for data in people_data:
        name = data.get("name")
        age = data.get("age")
        if name:
            person = Person(name, age)
            person.assign_gender("male" if data.get("wife") else "female")
            person_list.append(person)

    for data in people_data:
        name = data.get("name")
        if name in Person.people:
            person = Person.people[name]
            if data.get("wife"):
                person.wife = Person.people.get(data["wife"])
            if data.get("husband"):
                person.husband = Person.people.get(data["husband"])

    return person_list
