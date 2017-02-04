# Purpose
The whSignupFormProtestSubmitter submits protest submissions to the White House email signup form which, as of this writing, appears on the homepage of whitehouse.gov.

# License
This content is distributed under [CC-0](https://creativecommons.org/publicdomain/zero/1.0/).

# Requirements
This script requires Python and the following modules:
- [requests](http://docs.python-requests.org/en/master/)
- random
- time

The latter to are part of the Python Standard Libary.  The Requests module you'll have to install yourself.  Directions for that can be found on the Requests site.

# Usage
The easiest thing to do is run whSignupFormProtestSubmitter from the command line

```
$ python whSignupFormProtestSubmitter.py
```

This will create 50 submissions from randomized email addresses and sleeping for a random interval between 1 and 30 seconds between submissions.  This sleep/delay is intentional for two reasons.  First, it will ensure submissions do not trigger some form of rate limiting.  Secondly, the intent of the script is deliberately NOT to create a DoS situation on the site.  We dont want to break their site, just fill their submission logs with protest submissions.

Use of a VPN or other tool to obscure your IP is recommended but outside the scope of this tool.