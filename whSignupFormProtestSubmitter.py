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
        'whitehouse.gov',
        'state.gov',
        'irs.gov',
        'epa.gov',
        'gop.com',
        'army.mil',
        'navy.mil',
        'af.mil',
        'congress.gov',
        'senate.gov'
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
        'formsarenotpetitions'
    ]

    return str.join('', [random.choice(localParts), '@', random.choice(domains)])


def frontPageForm():
    targetURL = 'https://forms.whitehouse.gov/webform/email-signup'

    dataPayload = {
        "submitted[email_address]": _buildFakeEmailAddress(),
        "submitted[zip_code]": _buildZipCode(),
        "form_id": "webform_client_form_111",
        "form_build_id": "form-43X7sWhYGJ1EdVKeroNYk0M2Wnv7I-Bp4qrOtulPg6A"
    }

    return {'targetURL': targetURL, 'dataPayload': dataPayload}


def gorsuchForm():
    targetURL = 'https://forms.whitehouse.gov/webform/scotus-form'

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
    targetURL = 'https://forms.whitehouse.gov/webform/trump-stands-with-israel'

    fname, lname = _buildName()

    dataPayload = {
        "submitted[first_name]": fname,
        "submitted[last_name]": lname,
        "submitted[e_mail_address]": _buildFakeEmailAddress(),
        "submitted[zip_code]": _buildZipCode(),
        "form_id": "webform_client_form_176",
        "form_build_id": "form-zsH6jltzBOSHwMFO5DyO0Ki9DSVWIjxVSxLydxlsSd0"
    }

    return {'targetURL': targetURL, 'dataPayload': dataPayload}


def womenForm():
    targetURL = 'https://forms.whitehouse.gov/webform/empowering-female-leaders'

    fname, lname = _buildName()

    dataPayload = {
        "submitted[first_name]": fname,
        "submitted[last_name]": lname,
        "submitted[e_mail_address]": _buildFakeEmailAddress(),
        "submitted[zip_code]": _buildZipCode(),
        "form_id": "webform_client_form_166",
        "form_build_id": "form-NqsMkzEZaaDlyQrTXOKzDh1K-R60re0e1pglFMgWIR4"
    }

    return {'targetURL': targetURL, 'dataPayload': dataPayload}

def workForm():
    targetURL = 'https://forms.whitehouse.gov/webform/get-involved'

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


def sendProtestSubmission(form):
    data = form()
    try:
        r = requests.post(data['targetURL'], data=data['dataPayload'])
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
            womenForm
        ]

        form = random.choice(forms)

        result = sendProtestSubmission(form)
        sleepTime = random.randint(1, 10)
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
