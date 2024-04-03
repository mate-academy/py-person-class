class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.spouse = None
        self.wife = None
        self.husband = None
        self.__class__.people[name] = self

    def set_spouse(self, spouse_name: str) -> None:
        if spouse_name in self.__class__.people:
            self.spouse = self.__class__.people[spouse_name]


def create_person_list(people: list) -> list:
    person_dict = {}
    person_list = []

    for person_data in people:
        name = person_data["name"]
        age = person_data["age"]
        person = Person(name, age)
        person_dict[name] = person
        person_list.append(person)

    for person_data in people:
        name = person_data["name"]
        spouse_name = person_data.get("wife") or person_data.get("husband")
        if spouse_name is not None:
            person = person_dict[name]
            spouse = person_dict[spouse_name]
            person.set_spouse(spouse_name)
            if "wife" in person_data:
                person.wife = spouse
            elif "husband" in person_data:
                person.husband = spouse
    return person_list
