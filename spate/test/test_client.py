from nose.plugins.attrib import attr

from spate import Client


class TestClient(object):

    TEST_SECRET = '153d49793c831974b36b5f3c4f24978b'
    TEST_KEY = 'f7f9e8cbf8317faca95270cac84e3d11'
    EXPECTED_SIGNATURE = '6c3cda883be1d318cee6cf733b48c32f727b2b25d95d4af97b8de988ee9d8a62'

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
