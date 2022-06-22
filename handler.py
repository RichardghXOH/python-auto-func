import requests
import os


IAM = os.environ['IAM']
FOLDER_ID = os.environ['FolderId']
list_url = 'https://compute.api.cloud.yandex.net/compute/v1/instances'
PARAMS = {
    "folderId": FOLDER_ID
}
HEADERS  = {
'Authorization': f'Bearer {IAM}'
}

list_url = 'https://compute.api.cloud.yandex.net/compute/v1/instances'
PARAMS = {
    "folderId": FOLDER_ID
}
HEADERS = {
    'Authorization': f'Bearer {IAM}'
}


def up_machine(instanceId):
    up_url = f'https://compute.api.cloud.yandex.net/compute/v1/instances/{instanceId}:start'
    response = requests.post(up_url, headers=HEADERS, params=PARAMS)
    return response


def get_machine_status():
    """

    :return:
    dict machine_id:machine_status
    """
    r = requests.get(url=list_url, headers=HEADERS, params=PARAMS)
    response = r.json()
    machine_status = {}
    amount_instancces = len(response['instances'])
    for inst_num in range(0, amount_instancces):
        machine_status.update({response['instances'][inst_num]['id']: response['instances'][inst_num]['status']})
    return machine_status


def restart_machines(req_machine_id='all'):
    if req_machine_id is None:
        return "Error: Not machine id"
    else:
        curr_machines_dict = get_machine_status()
    if req_machine_id is 'all':
        for id in curr_machines_dict.keys():
            up_machine(id)
    else:
        return 'testing'





def handler(event, context):
    event.
    return {
        'statusCode': 200,
        'body': restart_machines()
    }
