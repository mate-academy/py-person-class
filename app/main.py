class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    # Очищаем словарь перед каждым запуском, как просит Люк
    Person.people = {}

    instances = [
        Person(person_dict["name"], person_dict["age"])
        for person_dict in people
    ]

    for person_dict in people:
        person_instance = Person.people[person_dict["name"]]
        for partner_type in ["wife", "husband"]:
            partner_name = person_dict.get(partner_type)
            if partner_name:
                setattr(
                    person_instance,
                    partner_type,
                    Person.people[partner_name]
                )

    return instances
