import requests
import random
import time

def _buildFakeEmailAddress():
    domains = [
        'trump.com',
        'trumpinternaltionalrealty.com',
        'donaldjtrump.com',
        'trumporg.com',
        'trumpuniversity.com',
        'tmgmt.com',
        '10minutemail.com',
        'eelmail.com',
        'einrot.com',
        'fleckens.hu',
        'getairmail.com',
        'grr.la',
        'guerrillamail.biz',
        'gustr.com',
        'harakirimail.com',
        'hulapla.de',
        'hushmail.com',
        'imgof.com',
        'imgv.de',
        'mailinator.com',
        'reconmail.com',
        'rhyta.com',
        's0ny.net',
        'sharklasers.com',
        'sogetthis.com',
        'soodonims.com',
        'stonerfans.com',
        'streetwisemail.com',
        'superrito.com',
        'suremail.info',
        'tafmail.com',
        'teewars.org',
        'teleworm.us',
        'thehighlands.co.uk',
        'tradermail.info',
        'trbvm.com',
        'value-mycar.co.uk',
        'yopmail.com',
        'zippymail.info',
        'zxcvbnm.co.uk',
        ]

    localParts = [
        'dumptrump',
        'banbannon',
        'h8fascism',
        'freemelania',
        'fred.douglass',
        'greenbowling',
        'kellyannesclearheels',
        'nicer4spicer',
        'mexicalijoe',
        'mu.slim',
        'giantmeteor2016',
        'freescience',
        'putinitinyou',
        'ivankadrinkyerblood',
        'SN.atch.grabber',
        'drumpfhouse',
        're.fugee',
        'australasia',
        'youcrane',
        'gldnshwrs',
        'factsschmacts'
    ]

    return str.join('', [random.choice(localParts), '@', random.choice(domains)])


def sendProtestSubmission(email):

    targetURL = 'https://forms.whitehouse.gov/webform/email-signup'

    dataPayload = {
        "submitted[email_address]": email,
        "submitted[zip_code]": "12345",
        "form_id": "webform_client_form_111",
        "form_build_id": "form-43X7sWhYGJ1EdVKeroNYk0M2Wnv7I-Bp4qrOtulPg6A"
    }

    r = requests.post(targetURL, data=dataPayload)
    return r.status_code


def fireTehLazers(iterations=5):
    for i in range(0,iterations):
        email = _buildFakeEmailAddress()
        result = sendProtestSubmission(email)
        sleepTime = random.randint(1,30)
        print(str(i) + " of " + str(iterations) + ": " + email + ", result code: " + str(result) + ". Next post in " + str(sleepTime) + " seconds.")
        time.sleep(sleepTime)

if __name__ == '__main__':
    fireTehLazers(50)