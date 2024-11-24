class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person_dict in people:
        # Create a Person instance and add it to the list
        person = Person(person_dict["name"], person_dict["age"])
        person_list.append(person)

    for person_dict in people:
        name = person_dict["name"]
        if "wife" in person_dict and person_dict["wife"]:
            person = Person.people[name]
            spouse = Person.people[person_dict["wife"]]
            person.wife = spouse
            spouse.husband = person

        elif "husband" in person_dict and person_dict["husband"]:
            person = Person.people[name]
            spouse = Person.people[person_dict["husband"]]
            person.husband = spouse
            spouse.wife = person
        return person_list
