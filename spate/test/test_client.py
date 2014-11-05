from nose.plugins.attrib import attr

from spate import Client


class TestClient(object):

    TEST_SECRET = '785b5984cfbe119af5cc0230d0cd2c2e'
    TEST_KEY = '13ca90c13121e0b76573d46032c7f18f'
    EXPECTED_SIGNATURE = 'e2f67f6cdb05d1146a9f3ac9b736b350175e268626cca16f11bc501dff3cae65'

    def test_signing(self):
        client = Client(self.TEST_KEY, self.TEST_SECRET)
        assert client.sign('SIGNATURE_CHECK') == self.EXPECTED_SIGNATURE

    def test_from_url(self):
        url = 'https://%s:%s@fake.spate.io' % (self.TEST_KEY, self.TEST_SECRET)
        client = Client.from_url(url)
        assert client.app_key == self.TEST_KEY
        assert client.app_secret == self.TEST_SECRET
        assert client.api_base == 'https://fake.spate.io'
        assert client.sign('SIGNATURE_CHECK') == self.EXPECTED_SIGNATURE

    @attr('network')
    def test_push_integration(self):
        client = Client(self.TEST_KEY, self.TEST_SECRET)
        resp = client.push('A simple test message', ['test_chan'])
        assert resp.response.status_code == 202

    @attr('network')
    def test_push_incorrect_secret(self):
        client = Client(self.TEST_KEY, 'abc')
        resp = client.push('A simple test message', ['test_chan'])
        assert resp.response.status_code == 401
