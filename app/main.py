class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[name] = self
        self.wife = None
        self.husband = None


def create_person_list(people: list) -> list:
    list_of_people = []
    for data in people:
        name = data["name"]
        age = data["age"]
        person = Person(name, age)
        list_of_people.append(person)

    for person in list_of_people:
        if person.name in Person.people:
            data = next((d for d in people if d["name"] == person.name), None)
            if "wife" in data and data["wife"] is not None:
                wife_name = data["wife"]
                wife = Person.people.get(wife_name)
                if wife:
                    person.wife = wife
                    wife.husband = person
            elif "husband" in data and data["husband"] is not None:
                husband_name = data["husband"]
                husband = Person.people.get(husband_name)
                if husband:
                    person.husband = husband
                    husband.wife = person
            else:
                if hasattr(person, "wife"):
                    delattr(person, "wife")
    return list_of_people
