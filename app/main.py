class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[name] = self

    @classmethod
    def add_spouse(cls, person: dict, spouse_name: str) -> None:
        spouse = cls.people.get(spouse_name)
        if spouse:
            if hasattr(person, "wife"):
                person.wife = spouse
                spouse.husband = person
            else:
                person.husband = spouse
                spouse.wife = person


def create_person_list(people: list) -> list:
    person_list = []
    for person_data in people:
        name = person_data["name"]
        age = person_data["age"]
        person = Person(name, age)
        person_list.append(person)
        spouse_key = "wife" if "wife" in person_data else "husband"
        spouse_name = person_data[spouse_key]
        if spouse_name:
            Person.add_spouse(person, spouse_name)
    return person_list
