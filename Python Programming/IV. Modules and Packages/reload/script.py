import changer
from importlib import reload

# This should print first version
changer.whichVersion()

# When the file in the changer module is changed and the message variable is changed to "second version" this will not reflect the changes here because the module is already loaded in the memory and the changes are not reflected here.

# To reflect the changes in the module we can use the reload function from the importlib module.

reload(changer)
changer.whichVersion() # now this should print the latest changes made in the module file.