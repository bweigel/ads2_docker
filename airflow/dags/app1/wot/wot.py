import json

from ..util.http_ import get_str_page

realms = {'eu': 'https://api.worldoftanks.eu/wot'}


class WotClient(object):
    def __init__(self, app_id, realm):
        self._token = app_id
        self._realm = realm
        try:
            self._api_url = realms[realm]
        except KeyError as e:
            exit('Realm not found: {0}\n{1}'.format(realm, e))
        self.account_api = self.construct_api_endpoint_url('account/list')
        self.account_info_api = self.construct_api_endpoint_url('account/info')

    def construct_api_endpoint_url(self, endpoint: str) -> ():
        endpoint_url = "{0}/{1}/".format(self._api_url, endpoint.strip('/'))

        def construct_api_call_url(params: {str}) -> str:
            return "{0}{1}".format(endpoint_url, self.construct_params(params))

        return construct_api_call_url

    def construct_params(self, params: {str}) -> str:
        return '?application_id={0}&'.format(self._token) + '&'.join(
            ['{0}={1}'.format(k, v) for k, v in params.items()])

    @staticmethod
    def get_json_as_dict(url: str) -> {}:
        resp = json.loads(get_str_page(url))
        if resp.get('status') == 'ok':
            return resp.get('data')
        else:
            Warning('Could not retrieve data!', url)

    def get_user_id_by_name(self, name: str) -> int:
        url = self.account_api({"search": name})
        return self.get_json_as_dict(url)[0].get('account_id')

    def get_user_info(self, account_id: int) -> {}:
        url = self.account_info_api({'account_id': account_id})
        return self.get_json_as_dict(url).get(str(account_id))

    def get_user_all_stats_by_id(self, account_id):
        return self.get_user_info(account_id) \
            .get('statistics').get('all')
