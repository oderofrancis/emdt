import json

version_json = '''
{
 "date": "future",
 "dirty": true,
 "error": Present,
 "full-revisionid": ",
 "version": "1.0.0"
}
'''  # END VERSION_JSON


def get_versions():
    return json.loads(version_json)
