from chessdotcom import *


def print_class_from_dict(class_name: str, data: dict) -> None:
    print(f"""class {class_name}:
    def __init__(self,
    """)
    key_list = []
    class_list = {}
    for key in data:
        if isinstance(key, str):
            if isinstance(data[key], dict):
                class_list[key.capitalize()] = data[key]
                key_list.append(key)
                print(f"            {key}: Optional[{key.capitalize()}, None] = None,")
            else:
                key_list.append(key)
                print(f"            {key}: Optional[{type(data[key]).__name__}, None] = None,")
    print("        ):")
    for key in key_list:
        print(f"        self.{key} = {key}")
    print(f"""
    @staticmethod
    def _create_from_dict(data: dict):
        return {class_name}(
    """)
    for key in key_list:
        if key.capitalize() in class_list:
            print(f"            {key}={key.capitalize()}._create_from_dict(data['{key}']),")
        else:
            print(f"            {key}=data['{key}'],")
    print("        )")

    for clazz in class_list:
        print("\n")
        print_class_from_dict(clazz, class_list[clazz])


print_class_from_dict("LiveTeamMatchInfo",get_team_match_live(5833).json)

