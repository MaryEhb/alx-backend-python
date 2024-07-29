#!/usr/bin/env python3
'''unittests for client.py'''
import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    '''test case for client.GithubOrgClient'''

    @parameterized.expand([
        ['google', {'login': "google"}],
        ['abc', {'login': "abc"}]
    ])
    @patch('client.get_json')
    def test_org(self, org, res, mock_get):
        ''' test that GithubOrgClient.org returns the correct value'''
        mock_get.return_value = res
        github_org_client = GithubOrgClient(org)
        self.assertEqual(github_org_client.org, res)
        mock_get.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org)
        )

    def test_public_repos_url(self):
        '''method to unit-test GithubOrgClient._public_repos_url'''
        with patch('client.GithubOrgClient.org',
                new_callable=PropertyMock) as mock:
            payload = {"repos_url": "something"}
            mock.return_value = payload
            test_class = GithubOrgClient('test')
            result = test_class._public_repos_url
            self.assertEqual(result, payload["repos_url"])


if __name__ == '__main__':
    unittest.main()
