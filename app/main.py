class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[name] = self

    def add_spouse(self, spouse_name: str) -> None:
        spouse = self.__class__.people.get(spouse_name)
        if spouse:
            if hasattr(self, "wife"):
                self.wife = spouse
                spouse.husband = self
            else:
                self.husband = spouse
                spouse.wife = self


def create_person_list(people: list) -> list:
    person_list = []
    for person_data in people:
        person = Person(person_data["name"], person_data["age"])
        person_list.append(person)

        spouse_key = "wife" if "wife" in person_data else "husband"
        if spouse_key in person_data:
            person.add_spouse(person_data[spouse_key])

    return person_list
