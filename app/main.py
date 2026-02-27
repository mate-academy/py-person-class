class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people) -> list:
    people_dict = {person["name"]: Person(person["name"], person["age"])
                   for person in people}

    # Link spouses
    for person in people:
        current_person = people_dict[person["name"]]

        # Check for wife
        wife_name = person.get("wife")
        if wife_name:
            wife_obj = people_dict[wife_name]
            current_person.wife = wife_obj
            wife_obj.husband = current_person

        # Check for husband
        husband_name = person.get("husband")
        if husband_name:
            husband_obj = people_dict[husband_name]
            current_person.husband = husband_obj
            husband_obj.wife = current_person

    return list(people_dict.values())
