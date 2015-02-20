#!/usr/bin/env python3

# This file contains the python3 tests for the Kubernetes Juju bundle.

import amulet
import os
import unittest
import yaml

seconds = 1800


class BundleIntegrationTest(unittest.TestCase):
    """ This class creates an integration test for deploying a bundle. """
    bundle = None

    @classmethod
    def setUpClass(cls):
        """ This method deploys the bundle. """

        if not cls.bundle:
            # Get the relative bundle path from the environment variable.
            cls.bundle = os.getenv('BUNDLE', 'bundles.yaml')
        # Create a path to the bundle based on this file's location.
        cls.bundle_path = os.path.join(os.path.dirname(__file__),
                                       '..',
                                       cls.bundle)
        # Normalize the path to the bundle.
        cls.bundle_path = os.path.abspath(cls.bundle_path)

        print('Deploying bundle: {0}'.format(cls.bundle_path))
        cls.deployment = amulet.Deployment()
        with open(cls.bundle_path, 'r') as bundle_file:
            contents = yaml.safe_load(bundle_file)
            cls.deployment.load(contents)
        try:
            cls.deployment.setup(seconds)
            cls.deployment.sentry.wait()
        except amulet.helpers.TimeoutError:
            message = 'Unable to set up environment in %d seconds.' % seconds
            amulet.raise_status(amulet.FAIL, msg=message)
        except:
            raise

    def kunits(self):
        """ Return a tuple of the relevant units. """
        return (self.deployment.sentry.unit['kubernetes/0'],
                self.deployment.sentry.unit['kubernetes/1'],
                self.deployment.sentry.unit['kubernetes-master/0'])

    def test_0_unit_existance(self):
        """ Test the unit existance. """
        assert self.deployment.sentry.unit.get('kubernetes/0', False)
        assert self.deployment.sentry.unit.get('kubernetes/1', False)
        assert self.deployment.sentry.unit.get('kubernetes-master/0', False)

    def test_1_relations(self):
        """ Test bundle relations. Errors will be thrown if relations fail. """
        kube0, kube1, km = self.kunits()
        # Get all the important relations from the bundle.
        etcd_relation = kube0.relation('etcd', 'etcd:client')
        master_relation = kube0.relation('api',
                                         'kubernetes-master:minions-api')
        minion_relation = km.relation('minions-api', 'kubernetes:api')
        return etcd_relation, master_relation, minion_relation

#    def test_2_http(self):
#        """ Test that kubernetes is responding to HTTP requests. """
#        km = self.deployment.sentry.unit['kubernetes-master/0']
#        km_address = km.info['public-address']
#        km_url = 'http://{0}:8080'.format(km_address)
#        print(km_url)
#        response = requests.get(km_url)
#        response.raise_for_status()
#        if 'Kubernetes' not in response.text:
#            message = 'Kubernetes is not responding at {0}.'.format(km_url)
#            amulet.raise_status(amulet.FAIL, msg=message)


if __name__ == '__main__':
    unittest.main()
