import getopt
import requests
import random
import sys
import time


def _buildName():
    fnames = [
        'Abraham',
        'Andrew',
        'Barack',
        'Benjamin',
        'Calvin',
        'Chester',
        'Dwight',
        'Franklin',
        'George',
        'Gerald',
        'Grover',
        'Harry',
        'Herbert',
        'James',
        'John',
        'Lyndon',
        'Martin',
        'Millard',
        'Richard',
        'Ronald',
        'Rutherford',
        'Theodore',
        'Thomas',
        'Ulysses',
        'Warren',
        'William',
        'Woodrow',
        'Zachary'
    ]

    lnames = [
        'Adams',
        'Arthur',
        'Buchanan',
        'Bush',
        'Carter',
        'Cleveland',
        'Clinton',
        'Coolidge',
        'Eisenhower',
        'Fillmore',
        'Ford',
        'Garfield',
        'Grant',
        'Harding',
        'Harrison',
        'Hayes',
        'Hoover',
        'Jackson',
        'Jefferson',
        'Johnson',
        'Kennedy',
        'Knox',
        'Lincoln',
        'Madison',
        'McKinley',
        'Monroe',
        'Nixon',
        'Obama',
        'Pierce',
        'Reagan',
        'Roosevelt',
        'Taft',
        'Taylor',
        'Truman',
        'Tyler',
        'VanBuren',
        'Washington',
        'Wilson'
    ]

    return (random.choice(fnames), random.choice(lnames))


def _buildZipCode():
    zipDigits = []

    for i in range(0, 5):
        zipDigits.append(str(random.randint(0, 9)))

    return ''.join(zipDigits)


def _buildFakeEmailAddress(fname=None, lname=None):

    domains = [
        'gmail.com',
        'yahoo.com',
        'hotmail.com',
        'trump.com',
        'trumpinternaltionalrealty.com',
        'donaldjtrump.com',
        'trumporg.com',
        'trumpuniversity.com',
        'tmgmt.com',
        'juno.com',
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
        'whitehouse.gov',
        'state.gov',
        'fcc.gov',
        'dot.gov',
        'irs.gov',
        'epa.gov',
        'gop.com',
        'army.mil',
        'navy.mil',
        'af.mil',
        'congress.gov',
        'senate.gov',
        'outlook.com',
        'kgb.net',
        'kkk.org',
        'aol.com',
        'live.com',
        'verizon.com',
        'earthlink.net',
        'comcast.net',
        'infowars.com',
        'naturalnews.com',
        'mindspring.com',
        'russianhookers.net'
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
        'ivankadanke',
        'SN.atch.grabber',
        'drumpfhouse',
        're.fugee',
        'australasia',
        'youcrane',
        'gldnshwrs',
        'factsschmacts',
        'smoochinmnuchin',
        'mike.penceive',
        'gorsucks',
        'de.voss',
        'donaldtrumpmakesmewannasmokecrack',
        'formsarenotpetitions',
        'refuse',
        'resist',
        'nonserviam',
        'vlad',
        'bvdobbs',
        'usck',
        'lies',
        'damnlies',
        'whathappenedtodrainingtheswamp',
        'yourwallisstupidandsoareyou'
    ]

    if fname and lname:
        # this basically creates a random boolean
        if random.randint(0,4):
            local = _generateEmailLocalFromName(fname, lname)
        else:
            local = random.choice(localParts)
    else:
        local = random.choice(localParts)

    address = str.join('', [local, '@', random.choice(domains)]).lower()

    print("Generated " + address)

    return address


def _generateEmailLocalFromName(fname, lname):
    r = random.randint(1, 3)
    if r == 1:
        local = str.join('', [fname[0], lname])
    elif r == 2:
        local = str.join('_', [fname, lname])
    else:
        local = str.join('.', [fname, lname])

    return local


def frontPageForm():
    targetURL = 'https://forms.whitehouse.gov/webform/email-signup?initialWidth=544&childId=forall-iframe-embed-1&parentUrl=https%3A%2F%2Fwww.whitehouse.gov'

    dataPayload = {
        "submitted[email_address]": _buildFakeEmailAddress(),
        "submitted[zip_code]": _buildZipCode(),
        "form_id": "webform_client_form_111",
        "form_build_id": "form-43X7sWhYGJ1EdVKeroNYk0M2Wnv7I-Bp4qrOtulPg6A"
    }

    return {'targetURL': targetURL, 'dataPayload': dataPayload}


def gorsuchForm():
    targetURL = 'https://forms.whitehouse.gov/webform/scotus-form?initialWidth=544&childId=forall-iframe-embed-1&parentUrl=https%3A%2F%2Fwww.whitehouse.gov%2Fsupport-nominee-gorsuch'

    fname, lname = _buildName()

    dataPayload = {
        "submitted[first_name]": fname,
        "submitted[last_name]": lname,
        "submitted[e_mail_address]": _buildFakeEmailAddress(),
        "submitted[zip_code]": _buildZipCode(),
        "form_id": "webform_client_form_106",
        "form_build_id": "form-sZV-iGQZ-ZjG8D9H_5SGIZfBSBEsGfiLx-mjVrXt20E"
    }

    return {'targetURL': targetURL, 'dataPayload': dataPayload}


def israelForm():
    targetURL = 'https://forms.whitehouse.gov/webform/trump-stands-with-israel?initialWidth=544&childId=forall-iframe-embed-1&parentUrl=https%3A%2F%2Fwww.whitehouse.gov%2Ftrump-stands-with-israel'

    fname, lname = _buildName()

    dataPayload = {
        "submitted[first_name]": fname,
        "submitted[last_name]": lname,
        "submitted[email]": _buildFakeEmailAddress(),
        "submitted[zip_code]": _buildZipCode(),
        "form_id": "webform_client_form_176",
        "form_build_id": "form-zsH6jltzBOSHwMFO5DyO0Ki9DSVWIjxVSxLydxlsSd0"
    }

    return {'targetURL': targetURL, 'dataPayload': dataPayload}


def womenForm():
    targetURL = 'https://forms.whitehouse.gov/webform/empowering-female-leaders?initialWidth=544&childId=forall-iframe-embed-1&parentUrl=https%3A%2F%2Fwww.whitehouse.gov%2Fsupport-empowering-female-leaders'

    fname, lname = _buildName()

    dataPayload = {
        "submitted[first_name]": fname,
        "submitted[last_name]": lname,
        "submitted[email]": _buildFakeEmailAddress(),
        "submitted[zip_code]": _buildZipCode(),
        "form_id": "webform_client_form_166",
        "form_build_id": "form-NqsMkzEZaaDlyQrTXOKzDh1K-R60re0e1pglFMgWIR4"
    }

    return {'targetURL': targetURL, 'dataPayload': dataPayload}

def workForm():
    targetURL = 'https://forms.whitehouse.gov/webform/get-involved?initialWidth=544&childId=forall-iframe-embed-1&parentUrl=https%3A%2F%2Fwww.whitehouse.gov%2Fsupport-american-back-to-work'

    fname, lname = _buildName()

    dataPayload = {
        "submitted[first_name]": fname,
        "submitted[last_name]": lname,
        "submitted[email_address]": _buildFakeEmailAddress(),
        "submitted[zip_code]": _buildZipCode(),
        "form_id": "webform_client_form_141",
        "form_build_id": "form-6kxJzAO-R2p9ejec8AywNsveIW9AnRlHbM1v19Gp2Ug"
    }

    return {'targetURL': targetURL, 'dataPayload': dataPayload}

def jointAddressForm():
    targetURL = 'https://forms.whitehouse.gov/webform/joint-address-congress-2017-signup?initialWidth=544&childId=forall-iframe-embed-1&parentUrl=https%3A%2F%2Fwww.whitehouse.gov%2Fjoint-address'

    fname, lname = _buildName()

    dataPayload = {
        "submitted[first_name]": fname + ' ' + lname,
        "submitted[email_address]": _buildFakeEmailAddress(fname, lname),
        "submitted[zip_code]": _buildZipCode(),
        "form_id": "webform_client_form_196",
        "form_build_id": "form-6kxJzAO-R2p9ejec8AywNsveIW9AnRlHbM1v19Gp2Ug"
    }

    return {'targetURL': targetURL, 'dataPayload': dataPayload}


def _buildMAGIdea():

    return "Remove Donald Drumpf from office."


def _buildState():

    return "District of Columbia"

def _buildCountry():

    return "United States"

def _buildComment():

    return "No matter how much money or power you have, Donald, she still won't love you."

def issueSurveyForm():
    targetURL = 'https://forms.whitehouse.gov/webform/joint-address-issues-survey?initialWidth=544&childId=forall-iframe-embed-1&parentUrl=https%3A%2F%2Fwww.whitehouse.gov%2Fjoint-address-issues-survey'

    fname, lname = _buildName()

    dataPayload = {
        "submitted[3_what_are_your_ideas_to_mae_america_great_again]": _buildMAGIdea(),
        "submitted[first_name]": fname,
        "submitted[last_name]": lname,
        "submitted[email_address]": _buildFakeEmailAddress(),
        "submitted[zip_code]": _buildZipCode(),
        "submitted[country]": _buildCountry(),
        "submitted[state]": _buildState(),
        "submitted[4_additional_comments]": _buildComment(),
        "form_id": "webform_client_form_206",
        "form_build_id": "form-qzHYQwgCHonDYAAgpQMnllOIuqyMGDPKddwUtJjp4LI"
    }

    return {'targetURL': targetURL, 'dataPayload': dataPayload}

def _buildUserAgent():
    agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
    ]
    return random.choice(agents)

def sendProtestSubmission(form):
    data = form()
    try:
        r = requests.post(data['targetURL'], headers={'User-agent': _buildUserAgent()}, data=data['dataPayload'])
    except Exception as err:
        print("Woops.  Something went sideways. " + err)

    return r.status_code


def fireTehLazers(iterations=5):
    for i in range(0, iterations):
        forms = [
            frontPageForm,
            gorsuchForm,
            workForm,
            israelForm,
            womenForm,
            issueSurveyForm,
            jointAddressForm
        ]

        form = random.choice(forms)

        result = sendProtestSubmission(form)
        sleepTime = random.randint(1, 600)
        print(str(i + 1) + " of " + str(iterations) + ": " + form.__name__ + ", result code: " + str(
            result) + ". Next post in " + str(sleepTime) + " seconds.")
        time.sleep(sleepTime)


def main(args):
    try:
        opts, args = getopt.getopt(args, "hi:", ["iterations=", "help"])
    except getopt.GetoptError:
        print('whSignupFormProtestSubmitter.py -i <number_of_submissions>')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-i", "--iterations") and isinstance(int(arg), int):
            iterations = int(arg)
            fireTehLazers(iterations)
        else:
            print('whSignupFormProtestSubmitter.py -i <number_of_submissions>')
            sys.exit(2)


if __name__ == '__main__':
    main(sys.argv[1:])
