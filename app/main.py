class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[name] = self

    def set_wife(self, wife: str) -> None:
        self.wife = wife

    def set_husband(self, husband: str) -> None:
        self.husband = husband


def create_person_list(people_list: list) -> list:
    person_instances = {}
    result = []

    for person in people_list:
        name = person["name"]
        age = person["age"]
        person_instance = Person(name, age)
        person_instances[name] = person_instance
        result.append(person_instance)

    for person_data in people_list:
        person_name = person_data["name"]
        person_instance = person_instances[person_name]

        wife_name = person_data.get("wife")
        if wife_name:
            wife_instance = person_instances[wife_name]
            person_instance.set_wife(wife_instance)

        husband_name = person_data.get("husband")
        if husband_name:
            husband_instance = person_instances[husband_name]
            person_instance.set_husband(husband_instance)

    return result
