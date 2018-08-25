# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import logging

from uniborg import Uniborg

logging.basicConfig(level=logging.INFO)

import os
if "APP_ID" not in os.environ and "API_HASH" not in os.environ:
    import sys
    print("Please fill in the required values from app.json "
          "Do not steal the values from the official application. "
          "Doing that WILL backfire on you. \nBot quitting.", file=sys.stderr)
    quit(1)

borg = Uniborg("stdborg", plugin_path="stdplugins", connection_retries=None)

borg.run_until_disconnected()
