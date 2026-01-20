class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

    def __str__(self) -> str:
        return f"Person(name={self.name}, age={self.age})"


def create_person_list(people: list) -> list:
    person_list = [
        Person(name=person["name"], age=person["age"])
        for person in people
    ]
    for person_data, person_instance in zip(people, person_list):
        wife_name = person_data.get("wife")
        husband_name = person_data.get("husband")

        wife = Person.people.get(wife_name)
        husband = Person.people.get(husband_name)

        if wife:
            person_instance.wife = wife

        if husband:
            person_instance.husband = husband
    return person_list
