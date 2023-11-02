from get_data import  get_data as get

def get_count_users(data:dict) -> int:
    """
    You are given dictionary. Find the number of users.

    Args:
        data(dict): data
    Returns:
        int: number of users
    """
    return data["info"]["results"]
data=get("randomuser_data.json")
print(get_count_users(data))