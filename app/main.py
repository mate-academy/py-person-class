class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    # Clear the dictionary in case the function is called multiple times
    Person.people = {}

    # Step 1: Create a list to hold our Person objects
    person_list = []

    # Loop through each dictionary in the input list and create a Person
    for person_dict in people:
        name = person_dict["name"]
        age = person_dict["age"]

        # Create the Person object
        person_obj = Person(name, age)
        person_list.append(person_obj)

    # Step 2: Go through the original data again to link wives and husbands
    for i in range(len(people)):
        person_dict = people[i]
        person_obj = person_list[i]

        # Check if the person has a wife
        if "wife" in person_dict and person_dict["wife"] is not None:
            wife_name = person_dict["wife"]

            person_obj.wife = Person.people[wife_name]

        # Check if the person has a husband
        if "husband" in person_dict and person_dict["husband"] is not None:
            husband_name = person_dict["husband"]
            person_obj.husband = Person.people[husband_name]

    return person_list
