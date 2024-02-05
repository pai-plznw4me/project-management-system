import json

from account.models import CustomUser


def apply_user(wbs_json):
    """
    twproject resource 정보를 플랫폼 유저 정보로 치환합니다.

    :param wbs_json: json
    ex)
        ret = open(filepath, 'r').read()
        json_ret = json.loads(ret)

    :return: json
    """
    new_resources = []
    users = CustomUser.objects.all()
    for ind, user in enumerate(users):
        new_resources.append({})
        new_resources[ind]['id'] = str(ind)
        new_resources[ind]['name'] = str(user.username)
    wbs_json['resources'] = new_resources
    return wbs_json
