import requests
import xmltodict
from collections import namedtuple
import re


class JoeSandbox:
    """
    JoeSandbox : Ingest malware data
    """
    data = namedtuple('JoeSandbox', ['domain', 'url', 'ipaddress', 'country', 'asn', 'md5sum'])
    base_url = 'https://www.joesandbox.com'

    @classmethod
    def recent_analysis(cls):
        url = '{0}/analysispaged/0'.format(cls.base_url)
        response = requests.get(url=url)
        if response.status_code != requests.codes.ok:
            return Exception('Unable to fetch data from: {0}'.format(url))
        # --
        return [int(a.groups()[0]) for a in re.finditer(b'href="/analysis/(\d+)/0/html"', response.content)]

    @classmethod
    def get_analysis(cls, joe_id):
        url = '{0}/analysis/{1}/0/irxml'.format(cls.base_url, joe_id)
        response = requests.get(url=url)
        if response.status_code != requests.codes.ok:
            return Exception('Unable to fetch data from: {0}'.format(url))
        # --
        return xmltodict.parse(response.content.decode('utf-8'))


if __name__ == '__main__':
    analysis = JoeSandbox.recent_analysis()
    print(len(analysis))
    # data = JoeSandbox.get_analysis(joe_id=42887)
    # print(data['analysis']['hashes']['sha256'])
    #
