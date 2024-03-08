import ctypes

class Person:
    people = {}
    def __init__(self, p_ple: list) -> None:
        if len(p_ple) == 0:
            return
        for human in p_ple:
            self.name = ""
            self.age = ""
            partner = list(human)[2]
            exec(f"self.{partner}=''")
            self.add_val(human)


    def add_val(self, human: dict) -> None:
        exec(f"{human['name']}=Person([])")
        exec(f"{human['name']}.name=human['name']")
        exec(f"{human['name']}.age=human['age']")
        # self.name = human["name"]
        # self.age = human["age"]
        partner = list(human)[2]
        exec(f"part_name = human['{partner}']")

        if locals()["part_name"] is not None:
            if locals()["part_name"] in Person.people:
                exec(f"{human['name']}.{partner}=Person.people[human['{partner}']]")
                for anti_partner in self.__dict__.keys():
                    if hasattr(Person.people[locals()["part_name"]],anti_partner):
                        exec(f"sec_part_name = Person.people[locals()['part_name']].{anti_partner}")
                        if locals()["sec_part_name"] == human['name']:
                            exec(f"Person.people[locals()['part_name']].{anti_partner} = locals()[human['name']]")
            else:
                exec(f"{human['name']}.{partner}=human['{partner}']")

        Person.people[human["name"]] = locals()[human["name"]]


def create_person_list(people: list) -> list:
    return [val for val in Person.people.values()]


