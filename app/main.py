class Person:
    # Shared master directory of all created instances
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        # Add this instance to the master directory
        Person.people[name] = self


def create_person_list(people: list) -> list:
    # Clear out the master directory to prevent cross-test data pollution
    Person.people.clear()
    # Initialize the return vessel
    ret_list = []
    # Check for missing args
    if not people:
        return ret_list
    # Pass 1 of 2 - create each person
    for person in people:
        # retrieve instance from master directory
        current_person = Person(person["name"], person["age"])
        ret_list.append(current_person)

    # Pass 2 of 2 - define relationship status
    for person in people:
        current_person = Person.people[person["name"]]
        if person.get("wife"):
            spouse_name = person["wife"]
            # store direct object link
            current_person.wife = Person.people[spouse_name]
        elif person.get("husband"):
            spouse_name = person["husband"]
            # store direct object link
            current_person.husband = Person.people[spouse_name]
    return ret_list
