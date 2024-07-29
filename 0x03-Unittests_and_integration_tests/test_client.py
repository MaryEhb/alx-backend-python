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

    @patch('client.get_json')
    def test_public_repos(self, mock_get):
        '''unit-test GithubOrgClient.public_repos'''
        payloads = [{"name": "google"}, {"name": "Twitter"}]
        mock_get.return_value = payloads

        with patch('client.GithubOrgClient._public_repos_url') as mock_public:
            mock_public.return_value = "done"
            test_class = GithubOrgClient('test')
            result = test_class.public_repos()
            expected = [p["name"] for p in payloads]
            self.assertEqual(result, expected)
            mock_get.called_with_once()
            mock_public.called_with_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, key, exp):
        ''' unit-test GithubOrgClient.has_license'''
        github_org_client = GithubOrgClient('google')
        client_with_licence = github_org_client.has_license(repo, key)
        self.assertEqual(client_with_licence, exp)


if __name__ == '__main__':
    unittest.main()
