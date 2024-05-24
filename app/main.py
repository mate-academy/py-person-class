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

    for i in range(len(persons)):
        person = persons[i]
        value = people_list[i]

        wife_name = value.get("wife")
        if wife_name:
            person.wife = Person.people.get(wife_name)

        husband_name = value.get("husband")
        if husband_name:
            person.husband = Person.people.get(husband_name)

    return persons
