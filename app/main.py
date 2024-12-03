class Person:
    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    new_people = []
    for person in people:
        new_people.append(Person(person["name"], person["age"]))

    for person_new in people:
        love = "husband" if person_new.get("husband") else "wife"
        love_name = person_new.get(love)
        if love_name:
            setattr(Person.people[person_new["name"]],
                    love,
                    Person.people[love_name])

    return new_people
