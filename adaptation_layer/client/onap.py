import requests
from error_handler import ResourceNotFound, NsNotFound, VnfNotFound,\
    Unauthorized, BadRequest, ServerError


class Client(object):
    def __init__(self):

        # add a info about ONAP IP and port - current local instance
        self._host = '10.254.184.187'
        self._port = 30274
        self._nbi_ver = 4
        # self._headers =

        self._base_path = 'http://{0}:{1}//nbi/api/v{2}'.format(self._host, self._port, self._nbi_ver)

    def _exec_get(self, url=None, params=None, header=None):

        try:
            resp = requests.get(url, params=params, headers=None)
        except Exception as e:
            print('before test1')
            raise ServerError(str(e))

        if resp.status_code in (200, 201, 202, 204, 206): # response code 206 was added
            print('response code: {}'.format(resp.status_code))  # for tests only
            return resp.json()
        elif resp.status_code == 400:
            print('response code: {}'.format(resp.status_code))  # for tests only
            raise BadRequest()
        elif resp.status_code == 401:
            print('response code: {}'.format(resp.status_code))  # for tests only
            raise Unauthorized()
        elif resp.status_code == 404:
            print('response code: {}'.format(resp.status_code))  # for tests only
            raise ResourceNotFound()
        else:
            error = resp.json()
            raise ServerError()

    # def _exec_post(self, url=None, data=None, json=None, headers=None):
    #
    #     try:
    #         resp = requests.post(url, data=data, json=json, headers=None)
    #     except Exception as e:
    #         raise ServerError(str(e))
    #
    #     if resp.status_code in (200, 201, 202, 204, 206):
    #         return resp.json()
    #     elif resp.status_code == 400:
    #         print('response code: {}'.format(resp.status_code))  # for tests only
    #         raise BadRequest()
    #     elif resp.status_code == 401:
    #         print('response code: {}'.format(resp.status_code))  # for tests only
    #         raise Unauthorized()
    #     elif resp.status_code == 404:
    #         print('response code: {}'.format(resp.status_code))  # for tests only
    #         raise ResourceNotFound()
    #     else:
    #         error = resp.json()
    #         raise ServerError()

    # def _exec_delete(self, url=None, data=None, json=None, headers=None):



    def ns_list(self):
        _url = '{0}/service'.format(self._base_path)
        return self._exec_get(_url)

    def ns_get(self, ns_id):
        _url = '{0}/service/{1}'.format(self._base_path, ns_id)
        try:
            return self._exec_get(_url)
        except ResourceNotFound:
            print('resource-not-found')
            raise NsNotFound(ns_id=ns_id)
    # exception doesnt work

    def ns_delete(self, ns_id):
        _url = '{0} {1}'.format(new_path, ns_id)
    try:
        return
    except:

    # def nf_list(self):

