#
#   Usage: python validate_pcr_ticket.py <JIRA login username> <API key> <ticket id>
#

from parser import *

import requests
from requests.auth import HTTPBasicAuth


def validate_pcr(api_url, login_id, api_key):
    response = requests.get(api_url, auth=HTTPBasicAuth(login_id, api_key))
    description = parse(response.text)
    Validation.validate(description)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        raise TypeError("Usage: python validate_pcr_ticket.py <JIRA login email> <API key> <ticket id>")
    login_id, api_key, ticket_id = sys.argv[1:]
    api_url = "https://bidgely.atlassian.net/rest/api/2/issue/{}".format(ticket_id)
    validate_pcr(api_url, login_id, api_key)
