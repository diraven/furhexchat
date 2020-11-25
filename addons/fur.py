__module_name__ = "FuR"
__module_version__ = "2.8"
__module_description__ = "Is supposed to help out with hatting."

# noinspection PyUnresolvedReferences,PyPackageRequirements,PyPep8
from config.addons.fur import API, init

import hexchat

api = API(hexchat)
init(api)
