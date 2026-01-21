class Person:
    people = {}  # Dictionary to store instances by name

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = int(age)  # Ensure age is an integer
        Person.people[name] = self  # Store instance by name


def create_person_list(people_list: list) -> None:
    # Step 1: Create all Person instances using list comprehension
    persons = [Person(p["name"], p["age"]) for p in people_list]

    # Step 2: Link spouses using dict.get()
    for person_dict in people_list:
        person = Person.people[person_dict["name"]]
        if person_dict.get("wife"):  # Using .get() avoids KeyError
            person.wife = Person.people[person_dict["wife"]]
        if person_dict.get("husband"):
            person.husband = Person.people[person_dict["husband"]]

    return persons
