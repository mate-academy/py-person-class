class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    Person.people.clear()
    person_list = [Person(person_dict["name"], person_dict["age"]) for person_dict in people]

    for person_dict in people:
        person = Person.people[person_dict["name"]]

        for relation in ("wife", "husband"):
            spouse_name = person_dict.get(relation)
            if spouse_name and spouse_name in Person.people:
                setattr(person, relation, Person.people[spouse_name])
                # Інакше не встановлюємо spouse, щоб при звертанні виникав AttributeError

    return person_list
