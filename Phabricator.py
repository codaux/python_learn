from phabricator import Phabricator

phab = Phabricator(host='https://farasoo.phabricator.ir:2443/', token='api-h2uk5pijfxxrew7gf5uvmsv56imm')  # This will use your ~/.arcrc file
phab.update_interfaces()