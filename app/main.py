class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_list: list) -> list:

        for person_dict in people_list:
            Person(person_dict["name"], person_dict["age"])

        for person_dict in people_list:
            person_instance = Person.people[person_dict["name"]]

            wife_name = person_dict.get("wife")
            if wife_name and wife_name in Person.people:
                person_instance.wife = Person.people[wife_name]

            husband_name = person_dict.get("husband")
            if husband_name and husband_name in Person.people:
                person_instance.husband = Person.people[husband_name]

        return list(Person.people.values())