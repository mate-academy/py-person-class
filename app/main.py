class Person:
    people = {}

<<<<<<< HEAD
def create_person_list(people_data):
    # First: create all Person instances
    for person_data in people_data:
        Person(person_data["name"], person_data["age"])
=======
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self
>>>>>>> 6dede77 (Solution)


def create_person_list(people: list) -> list:
    # First: create all Person instances
<<<<<<< HEAD
    for person_data in people_data:
        Person(person_data["name"], person_data["age"])

    # Second: link wife/husband
    # Use Person.people.get() to find the spouse
=======
    for person_data in people:
        Person(person_data["name"], person_data["age"])

    for person_data in people:
        person = Person.people[person_data["name"]]

        wife_name = person_data.get("wife")
        if wife_name:  # if not None
            person.wife = Person.people.get(wife_name)

        husband_name = person_data.get("husband")
        if husband_name:  # if not None
            person.husband = Person.people.get(husband_name)
>>>>>>> 6dede77 (Solution)

    # Return list of Person instances
    return list(Person.people.values())
