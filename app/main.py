class Person:
    people = {}  # Class attribute to store Person instances

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.wife = None  # Initialize wife attribute as None
        self.husband = None  # Initialize husband attribute as None

        # Add this instance to the people dictionary
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person_data in people:
        name = person_data["name"]
        age = person_data["age"]
        person = Person(name, age)

        # Check if the person is married
        if "wife" in person_data and person_data["wife"] is not None:
            wife_name = person_data["wife"]
            wife = Person.people.get(wife_name)
            if wife is not None:
                person.wife = wife
                wife.husband = person

        if "husband" in person_data and person_data["husband"] is not None:
            husband_name = person_data["husband"]
            husband = Person.people.get(husband_name)
            if husband is not None:
                person.husband = husband
                husband.wife = person

        person_list.append(person)

    return person_list
