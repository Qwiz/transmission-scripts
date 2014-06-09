# !/usr/bin/env python

from os import getenv
from ConfigParser import SafeConfigParser
# from notification.pushover import Pushover

def main():
    transmission_variable_list = [
        'TR_APP_VERSION',
        'TR_TIME_LOCALTIME',
        'TR_TORRENT_DIR',
        'TR_TORRENT_HASH',
        'TR_TORRENT_ID',
        'TR_TORRENT_NAME'
    ]
    transmission_variables = {var_name.lower(): getenv(var_name) for var_name in transmission_variable_list}
    config = SafeConfigParser()
    config.read("/var/lib/transmission-daemon/scripts/settings.conf")

    if config.items("common")["debug"]:
        debug = True

    if config.items("notification")["enabled"] == "1":
        import notification


    # ntype = config.get('notification','type')
    # engine = __import__('notification',ntype)



    # try:

    # settings = {config.get()}
    # print transmission_variables.items
    #message = "Work dir: " + str(work_dir) + str(u'\x0a')
    #for section in config.sections():
    #	message = message + section + str(u'\x0a')
    #for key, val in common_settings:
    #	message = message + key


    # if notification_settings["engine"].lower() == "pushover":
    #     api_key = notification_settings["api_token"]
    #     user_key = notification_settings["user_token"]
    #     push = Pushover(user_key, api_key, title="Debug message", message=message)
    #     push.sendmessage()

if __name__ == '__main__':
    main()
