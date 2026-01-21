class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self
        self.wife = None
        self.husband = None


def create_person_list(people: list) -> list:
    list_of_people = [Person(data["name"], data["age"]) for data in people]

    for person in list_of_people:
        if person.name in Person.people:
            data = next((d for d in people if d["name"] == person.name), None)
            if data.get("wife"):
                wife_name = data["wife"]
                wife = Person.people.get(wife_name)
                if wife:
                    person.wife = wife
                    wife.husband = person
            elif data.get("husband"):
                husband_name = data["husband"]
                husband = Person.people.get(husband_name)
                if husband:
                    person.husband = husband
                    husband.wife = person
            else:
                if hasattr(person, "wife"):
                    delattr(person, "wife")
    return list_of_people
