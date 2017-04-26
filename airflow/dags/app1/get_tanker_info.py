import json

from .wot.wot import WotClient
from .util.kms import kms_decrypt_token

ENCRYPTED_APP_ID = 'AQECAHhGzpV8mQljdA8TKn6ES9Tut5So2p1aU1owbT61BvTSSgAAAH4wfAYJKoZIhvcNAQcGoG8wbQIBADBoBgkqhkiG9w0B' \
                   'BwEwHgYJYIZIAWUDBAEuMBEEDItA7huGm/2I1ll2/AIBEIA7PYu2OMlSDEGSPpkUf8eHrL6tFw36VZ5N9Pq/wMmkVT49QtwF' \
                   'MtdXSdtvQzsrNuI7alojg6TWqe46HOg='

APP_ID = kms_decrypt_token(ENCRYPTED_APP_ID)


def write_wot_stats():
    client = WotClient(APP_ID, 'eu')

    userid = client.get_user_id_by_name('HerrKerian23')
    with open('user_info.json', 'a') as fo:
        fo.write(json.dumps(client.get_user_all_stats_by_id(userid)))
        fo.write("\n")

if __name__ == "__main__":
    write_wot_stats()