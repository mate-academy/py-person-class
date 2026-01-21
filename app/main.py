class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = []
    for person in people:
        class_person = Person(person["name"], person["age"])
        result.append(class_person)
    for index, person in enumerate(people):
        wife_or_husband = list(person.keys())[-1]
        if person[wife_or_husband] is None:
            continue
        setattr(
            result[index],
            wife_or_husband,
            Person.people.get(person[wife_or_husband])
        )

    return result
