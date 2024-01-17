class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[name] = self

    def set_spouse(self, spouse: str) -> None:
        if spouse:
            if isinstance(spouse, Person):
                self.husband = spouse
                spouse.wife = self


def create_person_list(people: list[dict]) -> list[Person]:
    person_list = []
    for person_data in people:
        name = person_data["name"]
        age = person_data["age"]
        person_instance = Person(name, age)
        person_list.append(person_instance)

        spouse_name = person_data.get("wife") or person_data.get("husband")
        if spouse_name is not None:
            spouse = Person.people.get(spouse_name)
            person_instance.set_spouse(spouse)

    return person_list
