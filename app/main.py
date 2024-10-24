class Person:
    people = {}  # Class attribute to store all instances by name

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.wife = None  # Initialize to None, can be set later
        self.husband = None  # Initialize to None, can be set later
        Person.people[name] = self  # Store instance in the class attribute


def create_person_list(people):
    # Step 1: Create Person instances for each person in the input list
    person_list = [Person(person["name"], person["age"]) for person in people]

    # Step 2: Set wife or husband attributes where applicable
    for person_dict in people:
        person_instance = Person.people[person_dict["name"]]
        if "wife" in person_dict:
            if person_dict["wife"] is not None:
                person_instance.wife = Person.people[person_dict["wife"]]
            else:
                del person_instance.wife
        elif "husband" in person_dict:
            if person_dict["husband"] is not None:
                person_instance.husband = Person.people[person_dict["husband"]]
            else:
                del person_instance.husband

    return person_list
