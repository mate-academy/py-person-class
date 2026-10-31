class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        wife = person.get("wife")
        husband = person.get("husband")

        if wife:
            couple_join(person["name"], wife, "wife")
        if husband:
            couple_join(person["name"], husband, "husband")

    return person_list


def couple_join(left_name: str, right_name: str, wife_husband: str) -> None:
    left = Person.people[left_name]
    right = Person.people[right_name]

    if wife_husband == "wife":
        left.wife = right
        right.husband = left
    else:
        left.husband = right
        right.wife = left
