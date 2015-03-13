from clint.textui import prompt
from path import path
import requests
import yaml
import sys


def handle_token(config, configfp):
    """ Prompt the user for the Jenkins token if it is not in config. """
    token = config['jenkins'].get('token', None)
    if token is None:
        token = prompt.query('You must enter a Jenkins token:')
        if token is None:
            raise RuntimeError("A token is required to use the API.")

        store = prompt.yn('Would you like to store your token?')
        if store is True:
            config['jenkins']['token'] = token
            cf = configfp / "config.yaml"
            with open(cf, 'w') as stream:
                yaml.safe_dump(config, stream)
    return token


def run_job(token, url, envs, callback, config, job, bundle, jenkins_api):
    """ Allow the running of jobs from other python methods.  """
    params = {
        'bundle': bundle,
        'callback_url': callback,
        'config': config,
        'envs': envs,
        'job_id': job,
        'token': token,
        'url': url,
    }
    response = requests.get(jenkins_api, params=params)
    return response


def jenkins_job(ctx, args, handle_token=handle_token):
    """ Get the token from config and the arguments to call the job. """
    token = handle_token(args.config, path(ctx['resources'].path))
    response = run_job(token, args.url, args.envs, args.callback,
                       args.description, args.job, args.bundle,
                       args.jenkins_api)
    if not response.ok:
        print("ERROR: The response back from the API was not OK!")
        print(response)
        sys.exit(1)
    print(response.url)
