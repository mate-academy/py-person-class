class Person:
    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.spouse = None
        Person.people[name] = self

    def set_spouse(self, spouse_name: str) -> None:
        spouse = Person.people.get(spouse_name)
        if spouse:
            self.spouse = spouse
            spouse.spouse = self
            if "wife" in vars(self).keys():
                setattr(self, "husband", spouse)
                setattr(spouse, "wife", self)
            else:
                setattr(self, "wife", spouse)
                setattr(spouse, "husband", self)


def create_person_list(people: list) -> list:
    person_list = []
    for person_data in people:
        name: str = person_data["name"]
        age: int = person_data["age"]
        person = Person(name, age)
        spouse_name = person_data.get("wife") or person_data.get("husband")
        if spouse_name:
            person.set_spouse(spouse_name)
        person_list.append(person)
    return person_list
