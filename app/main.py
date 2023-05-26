class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list[Person]:
    spouse_types: set[str] = {"wife", "husband"}
    for person in people:
        if person["name"] in Person.people:
            continue
        current_person: Person = Person(person["name"], person["age"])
        spouse_type: set = (spouse_types & person.keys())
        if len(spouse_type) < 1 or person.get(next(iter(spouse_type))) is None:
            continue
        spouse_name: str = person.get(next(iter(spouse_type)))
        if spouse_name not in Person.people:
            spouse_info = next((current_person
                                for current_person in people
                                if current_person["name"] == spouse_name),
                               None)
            Person(spouse_info["name"], spouse_info["age"])
        spouse_person: Person = Person.people[spouse_name]
        setattr(current_person, next(iter(spouse_type)),
                spouse_person)
        setattr(spouse_person, next(iter(spouse_types - spouse_type)),
                current_person)
    return list(Person.people.values())
