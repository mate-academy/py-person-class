class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    list_of_people = [Person(person_data["name"], person_data["age"])
                      for person_data in people]

    for person_data in people:
        name = person_data["name"]
        person = Person.people[name]

        if person_data.get("wife"):
            wife_name = person_data.get("wife")
            person.wife = Person.people[wife_name]

        if person_data.get("husband"):
            husband_name = person_data.get("husband")
            person.husband = Person.people[husband_name]
    return list_of_people
