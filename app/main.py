class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        Person.people[name] = self

    def set_spouse(self, spouse_name: str) -> None:
        if spouse_name in Person.people:
            spouse = Person.people[spouse_name]
            if spouse.age < self.age:
                self.wife = spouse
                spouse.husband = self
            else:
                self.husband = spouse
                spouse.wife = self


def create_person_list(people: list) -> None:
    person_list = []
    for person in people:
        per = Person(person["name"], person["age"])
        spouse_key = "wife" if "wife" in person else "husband"
        if spouse_key in person:
            per.set_spouse(person[spouse_key])
        person_list.append(per)
    return person_list
