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
    result = []

    for person_dict in people_list:
        name = person_dict["name"]
        age = person_dict["age"]
        person_object = Person(name, age)
        result.append(person_object)

    for person_object in result:
        for person_dict in people_list:
            if person_dict["name"] == person_object.name:
                wife_name = person_dict.get("wife")
                if wife_name:
                    for wife_instance in result:
                        if wife_instance.name == wife_name:
                            person_object.set_wife(wife_instance)

                husband_name = person_dict.get("husband")
                if husband_name:
                    for husband_instance in result:
                        if husband_instance.name == husband_name:
                            person_object.set_husband(husband_instance)

    return result
