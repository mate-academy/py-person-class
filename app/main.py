class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person_data in people:
        person = Person(name=person_data["name"], age=person_data["age"])
        person_list.append(person)
    for person_data in people:
        person = Person.people[person_data["name"]]
        spouse_name = person_data.get("wife") or person_data.get("husband")

        if spouse_name:
            spouse = Person.people.get(spouse_name)
            if spouse:
                if person_data.get("wife"):
                    person.wife = spouse
                    spouse.husband = person
                elif person_data.get("husband"):
                    person.husband = spouse
                    spouse.wife = person

    for person in person_list:
        if person.wife is None:
            delattr(person, "wife")
        if person.husband is None:
            delattr(person, "husband")

    return person_list
