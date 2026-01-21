class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_data: list) -> list:
    people_list = []

    for person_data in people_data:
        name = person_data["name"]
        age = person_data["age"]
        person = Person(name, age)
        people_list.append(person)

    for person_data in people_data:
        person = Person.people[person_data["name"]]
        wife_name = person_data.get("wife")
        husband_name = person_data.get("husband")

        if wife_name:
            person.wife = Person.people[wife_name]
            person.wife.husband = person
        elif husband_name:
            person.husband = Person.people[husband_name]
            person.husband.wife = person

    return people_list
