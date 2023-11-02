from get_data import get_data as get

def get_email(data:dict) -> list:
    """
    Take the email of the users and return the list.

    Args:
        data(dict): data
    Returns:
        list: users email
    """
    l=[]
    for i in data["results"]:
        l.append(i['email'])
    return l
data=get("randomuser_data.json")
print(get_email(data))