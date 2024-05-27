class Person:
    people = {}

    def __init__(self, name: str, age: int, *args) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_list: list) -> list[Person]:
    persons = [
        Person(temp_person["name"], temp_person["age"])
        for temp_person in people_list
    ]

    for people in range(len(persons)):
        person = persons[people]
        value = people_list[people]

        if wife_name := value.get("wife"):
            person.wife = Person.people.get(wife_name)

        if husband_name := value.get("husband"):
            person.husband = Person.people.get(husband_name)

    return persons
