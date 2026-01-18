class Person:
    def __init__(self, name, age):

        self.name = name
        self.age = age
        self.spouse = None

    def __repr__(self):

        spouse_info = f", Spouse: {self.spouse.name}" if self.spouse else ""
        return f"Person(Name: {self.name}, Age: {self.age}{spouse_info})"


def create_person_list(people_data):
    person_dict = {}
    for person in people_data:
        name = person["name"]
        age = person["age"]
        person_dict[name] = Person(name, age)

    for person in people_data:
        name = person["name"]
        spouse_name = person.get("wife") or person.get("husband")
        if spouse_name:
            if spouse_name in person_dict:
                person_dict[name].spouse = person_dict[spouse_name]
            else:
                raise ValueError(
                    f"Error for '{name}': Spouse name '{spouse_name}' not found in the data."
                )

        return list(person_dict.values())