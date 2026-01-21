class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    list_of_people = []
    for any_person in people:
        person = Person(
            name=any_person["name"],
            age=any_person["age"]
        )

        if any_person.get("wife") is not None:
            person.wife = any_person.get("wife")

        if any_person.get("husband") is not None:
            person.husband = any_person.get("husband")

        list_of_people.append(person)

    for any_person in list_of_people:
        if hasattr(any_person, "wife"):
            any_person.wife = any_person.people[any_person.wife]

        if hasattr(any_person, "husband"):
            any_person.husband = any_person.people[any_person.husband]

    return list_of_people
