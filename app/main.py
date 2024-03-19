class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[name] = self

    def set_spouse(self, spouse_name: str) -> None:
        spouse = self.__class__.people.get(spouse_name)
        if spouse:
            if "wife" in self.__dict__:
                self.wife = spouse
                spouse.husband = self
            else:
                self.husband = spouse
                spouse.wife = self


def create_person_list(people_list: list) -> list:
    person_list = []
    for person_data in people_lis
        name = person_data["name"]
        age = person_data["age"]
        spouse_name = person_data.get("wife") or person_data.get("husband")
        person_instance = Person(name, age)
        person_list.append(person_instance)
        if spouse_name:
            person_instance.set_spouse(spouse_name)
    return person_list
