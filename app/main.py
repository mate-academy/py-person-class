class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

def create_person_list(people_data: list[dict]) -> list[Person]:
    person_list = [Person(i["name"], i["age"]) for i in people_data]

    for i in people_data:
        person = Person.people[i["name"]]

        wife_name = i.get("wife")
        husband_name = i.get("husband")

        if wife_name:
            person.wife = Person.people[wife_name]
        if husband_name:
            person.husband = Person.people[husband_name]

    return person_list
