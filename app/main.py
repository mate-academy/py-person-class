class Person:
    # Class attribute to store all Person instances
    people = {}

    def __init__(self, name: str, age: int) -> None:
        # Initialize basic attributes
        self.name = name
        self.age = age

        # Add this instance to the people dictionary
        Person.people[name] = self


def create_person_list(people: list) -> list:
    # Clear the Person.people dictionary to avoid memory leaks and incorrect references
    Person.people.clear()

    # Create Person instances first
    person_list = []
    for person_dict in people:
        name = person_dict["name"]
        age = person_dict["age"]

        # Create Person instance
        person = Person(name, age)
        person_list.append(person)

    # Set relationship attributes
    for i, person_dict in enumerate(people):
        person = person_list[i]

        # Check for wife attribute
        if "wife" in person_dict and person_dict["wife"] is not None:
            wife_name = person_dict["wife"]
            setattr(person, "wife", Person.people[wife_name])

        # Check for husband attribute
        if "husband" in person_dict and person_dict["husband"] is not None:
            husband_name = person_dict["husband"]
            setattr(person, "husband", Person.people[husband_name])

    return person_list
