#!/usr/bin/python
 
import sys, os, json, traceback, re, time
from avi.sdk.avi_api import ApiSession

def parse_avi_params(argv):
    if len(argv) != 2:
        return {}
    script_parms = json.loads(argv[1])
    return script_parms

def create_avi_endpoint():
    token=os.environ.get('API_TOKEN')
    user=os.environ.get('USER')
    # tenant=os.environ.get('TENANT')
    return ApiSession.get_session(os.environ.get('DOCKER_GATEWAY'), user, token=token,
                                  tenant='admin')
                                  


# Script entry

if __name__ == "__main__":
    script_parms = parse_avi_params(sys.argv)
    try:
        admin_session = create_avi_endpoint()
        print(("vs name is %s" % (script_parms['obj_name'])))
        print(("vs uuid is %s" % (script_parms['events'][0]['obj_uuid'])))
        result_vs = admin_session.get(path='virtualservice/' + script_parms["events"][0]["obj_uuid"]).json()
        result_vs['traffic_enabled'] = 'False'
#         print(result_vs)
        admin_session.put(path='virtualservice/' + script_parms["events"][0]["obj_uuid"], data=result_vs)
#         result_vs = admin_session.get(path='virtualservice/' + script_parms["events"][0]["obj_uuid"]).json()
#         print(result_vs)

    except Exception:
        print('WARNING: Script did not work properly')