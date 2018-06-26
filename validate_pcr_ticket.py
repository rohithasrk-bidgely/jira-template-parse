#
#   Usage: python validate_pcr_ticket.py <JIRA login username> <API key> <ticket id>
#
import sys
from parser import *

import requests
from requests.auth import HTTPBasicAuth


def validate_pcr(api_url, login_id, api_key):
    response = requests.get(api_url, auth=HTTPBasicAuth(login_id, api_key))
    if 'preprod' in response.text.lower():
        sys.stdout.write("Prod PCR has a term Pre prod in it. Please check and update.\n")
        sys.exit(1)
    description = parse(response.text)
    Validation.validate(description)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        raise TypeError("Usage: python validate_pcr_ticket.py <JIRA login email> <API key> <ticket id>")
    login_id, api_key, ticket_id = sys.argv[1:]
    api_url = "https://bidgely.atlassian.net/rest/api/2/issue/{}".format(ticket_id)
    try:
        validate_pcr(api_url, login_id, api_key)
    except ValueError as e:
        sys.stdout.write(str(e))
        sys.exit(1)
