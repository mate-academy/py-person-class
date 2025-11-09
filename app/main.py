class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.update_people(name, self)

    @classmethod
    def update_people(cls, name: str, self: "Person") -> None:
        cls.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}
    people_dict = {}
    people_list = []

    if len(people) > 0:
        for person in people:
            family_name = None
            if person.get("wife") or person.get("husband"):
                family_name = ""
                if person.get("wife"):
                    family_name = person["wife"]
                elif person.get("husband"):
                    family_name = person["husband"]

            people_dict[person["name"]] = {
                "person": Person(person["name"], person["age"]),
                "family": {
                    "wife": 1 if person.get("wife") else 0,
                    "husband": 1 if person.get("husband") else 0,
                    "name": family_name
                }
            }

    if len(people_dict) > 0:
        for person in people_dict:
            if people_dict[person]["family"]["name"]:
                relation = "husband"
                if people_dict[person]["family"]["wife"] == 1:
                    relation = "wife"

                relation_name = people_dict[person]["family"]["name"]
                setattr(
                    people_dict[person]["person"],
                    relation,
                    Person.people[relation_name]
                )

            people_list.append(people_dict[person]["person"])

    return people_list
