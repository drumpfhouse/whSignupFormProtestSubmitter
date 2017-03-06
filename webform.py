"""
Defines a Webform class which defines the location (targetURL) and dictionary of fields and values which will
be submitted.

Previously this was implemented as a function as seen below.

def frontPageForm():
    targetURL = 'https://forms.whitehouse.gov/webform/email-signup?initialWidth=544&childId=forall-iframe-embed-1&parentUrl=https%3A%2F%2Fwww.whitehouse.gov'

    dataPayload = {
        "submitted[email_address]": _buildFakeEmailAddress(),
        "submitted[zip_code]": _buildZipCode(),
        "form_id": "webform_client_form_111",
        "form_build_id": "form-43X7sWhYGJ1EdVKeroNYk0M2Wnv7I-Bp4qrOtulPg6A"
    }

    return {'targetURL': targetURL, 'dataPayload': dataPayload}
"""


class Webform:
    targetURL = ''
    dataPayload = {}

    def __init__(self, targetURL = None, dataPayload = {}):
        self.targetURL = targetURL
        self.dataPayload = dataPayload

    """
    Returns the content of the form as a dictionary of targetURL and dataPayload.
    """
    def getData(self):
        return {'targetURL': self.targetURL, 'dataPayload': self.dataPayload}