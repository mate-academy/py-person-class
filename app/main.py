class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    @classmethod
    def add_person(cls, person_instance: "Person") -> None:
        cls.people[person_instance.name] = person_instance

    @classmethod
    def get_person(cls, name: str) -> "Person":
        return cls.people.get(name)


def create_people(people: list) -> list:
    person_instances = []
    for person_data in people:
        name = person_data["name"]
        age = person_data["age"]
        person = Person(name, age)
        Person.add_person(person)
        person_instances.append(person)
    return person_instances


def set_spouses(people: list) -> None:
    for person_data in people:
        name = person_data["name"]
        person_instance = Person.get_person(name)
        spouse = person_data.get("wife") or person_data.get("husband")
        if spouse:
            spouse_instance = Person.get_person(spouse)
            if "wife" in person_data:
                person_instance.wife = spouse_instance
            elif "husband" in person_data:
                person_instance.husband = spouse_instance


def create_person_list(people: list) -> list:
    person_instances = create_people(people)
    set_spouses(people)
    return person_instances
