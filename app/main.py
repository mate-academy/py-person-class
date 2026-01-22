class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = int(age)
        Person.people[name] = self

    def __repr__(self):
        return f"Person(name={self.name!r}, age={self.age!r})"


def create_person_list(people: list[dict]) -> list[Person]:
    Person.people.clear()

    instances = [Person(name=p["name"], age=p["age"]) for p in people]

    for p in people:
        person = Person.people[p["name"]]
        for spouse_key in ("wife", "husband"):
            spouse_name = p.get(spouse_key)
            if spouse_name:
                if spouse_name not in Person.people:
                    raise ValueError(
                        f"У даних вказано {spouse_key}={spouse_name}, "
                        f"але такої особи немає у списку."
                    )
                setattr(person, spouse_key, Person.people[spouse_name])
                break

    return instances
