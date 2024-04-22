class Person:
    people = {}

    def __init__(self, name: str, age: int | None) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self

    @classmethod
    def create_or_get(cls, name: str, age: int = None) -> "Person":
        if name in cls.people:
            person_instance = cls.people[name]
            person_instance.age = age
        else:
            person_instance = cls(name, age)
        return person_instance


def create_person_list(people_data: list) -> list:
    person_list = []
    for person_data in people_data:
        person_instance = Person.create_or_get(
            person_data["name"],
            person_data.get("age")
        )

        if person_data.get("wife"):
            person_instance.wife = Person.create_or_get(
                person_data["wife"]
            )

        if person_data.get("husband"):
            person_instance.husband = Person.create_or_get(
                person_data["husband"]
            )

        person_list.append(person_instance)

    return person_list
