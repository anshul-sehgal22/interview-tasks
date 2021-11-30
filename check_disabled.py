import status_data
import json
import os


def get_uuid():
    #aws lambda list-event-source-mappings | jq -r '.EventSourceMappings[] | select(.EventSourceArn | startswith("arn:aws:kinesis")) | .UUID'
    os.system()
    uuid=['231960e8-14b7-49eb-a160-76cc1a78edbb', '231960e8-14b7-49eb-a160-76cc1a78edbc', '231960e8-14b7-49eb-a160-76cc1a78edbd']
    return uuid


def get_status(uuid):
    if uuid == "231960e8-14b7-49eb-a160-76cc1a78edbb":
        return status_data.status1
    elif uuid == "231960e8-14b7-49eb-a160-76cc1a78edbc":
        return status_data.status2
    elif uuid == "231960e8-14b7-49eb-a160-76cc1a78edbd":
        return status_data.status3
    else:
        return "No match"


def enabler(uuid):
    print("aws lambda update-event-source-mapping --uuid {} --enabled".format(uuid))


for uuid in get_uuid():
    response = json.loads(get_status(uuid))
    state = response['State']
    if state == 'Disabled':
        print("You should enable {}".format(uuid))
        enabler(uuid)





