class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

    @classmethod
    def reset_people(cls) -> None:
        cls.people.clear()


def create_person_list(people_data: list[dict]) -> list[Person]:
    Person.reset_people()

    person_instances = [
        Person(data["name"], data["age"]) for data in people_data
    ]

    for data in people_data:
        current_person = Person.people[data["name"]]
        spouse_name = data.get("wife") or data.get("husband")

        if spouse_name:
            spouse_instance = Person.people.get(spouse_name)
            if spouse_instance:
                if "wife" in data:
                    current_person.wife = spouse_instance
                    spouse_instance.husband = current_person
                elif "husband" in data:
                    current_person.husband = spouse_instance
                    spouse_instance.wife = current_person

    return person_instances
