import json

version_json = '''
{
 "date": "2024-12-02T14:23:16+0200",
 "dirty": false,
 "error": null,
 "full-revisionid": "Not Deployed",
 "version": "1.0.0"
}
'''  # END VERSION_JSON


def get_versions():
    return json.loads(version_json)
