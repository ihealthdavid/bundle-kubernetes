from clint import resources
from path import path
from subparse import CLI
import logging
import yaml


def make_context(cli, args):
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    return dict(resources=resources.user,
                logger=logger)


def yaml_load(fp):
    with open(fp) as stream:
        return yaml.safe_load(stream)


def genopts(parser):
    fn = 'config.yaml'
    resources.init('kubecharm', 'kfc')
    rpath = path(resources.user.path) / fn
    if not rpath.exists():
        resources.user.write(fn, '---\njenkins: {}\n')

    parser.add_argument(
        '--config',
        default=yaml_load(rpath),
        help='The configuration file to use for the kfc commands.',
        type=yaml_load
        )


cli = CLI(version='0.0', context_factory=make_context)
cli.add_generic_options(genopts)
main = cli.run


@cli.command('kubecharm.bundle:test_all_bundles')
def test_all_bundles(parser):
    """
    Trigger a bundle test job on for each bundle defined in the
    specs/matrix.yaml file.
    """
    default_matrix = 'specs/matrix.yaml'
    parser.add_argument(
        '-m',
        '--matrix',
        action='store',
        default=default_matrix,
        help='The path to the matrix file that contains the permutations of'
             ' the bundles to test.',
        type=path,
    )


@cli.command('kubecharm.bundle:generate')
def generate_bundles(parser):
    """
    Set up the command l
    Generate all the combinations of bundles from the matrix file, basing the
    bundle on the template file, storing the output in a directory.
    """
    default_matrix = 'specs/matrix.yaml'
    default_template = 'bundles.yaml'
    default_output = 'specs'
    parser.add_argument(
        '-m',
        '--matrix',
        action='store',
        default=default_matrix,
        help='The path to the matrix file that contains the permutations of'
             ' kubernetes and juju charms to generate bundles from.',
        type=path,
    )
    parser.add_argument(
        '-t',
        '--template',
        action='store',
        default=default_template,
        help='The relative path to the bundle to use as the template '
             ' (the default is bundles.yaml).',
        type=path,
    )
    parser.add_argument(
        '-o',
        '--output',
        action='store',
        default=default_output,
        help='The relative path to the directory where bundles are written.',
        type=path,
    )


@cli.command('kubecharm.ci:jenkins_job')
def jenkins_job(parser):
    """
    Trigger a charm test build on the remote jenkins slave
    """
    api_url = 'http://juju-ci.vapour.ws:8080/job/charm-bundle-test-wip/buildWithParameters'

    parser.add_argument(
        '-a',
        '--jenkins-api',
        action='store',
        default=api_url,
        help='The URL to the jenkins server and path to the api endpoint.',
        type=path,
    )
    parser.add_argument(
        '-b',
        '--bundle',
        action='store',
        default='',
        help='The relative path to the bundle to deploy. By default the tools'
             ' will deploy bundles.yaml in the main bundle directory.',
        type=path,
    )
    parser.add_argument(
        '-c',
        '--callback',
        default='',
        help='The url called after the test run is complete to report the'
             ' results of the test. Defaults to none, mostly used by other'
             ' tools.',
    )
    parser.add_argument(
        '-d',
        '--description',
        default='',
        help='The human readable description of the test being run that will'
             ' show up in the test results table. If not set the bundle that'
             ' was run will show up to indicate what was run.',
    )
    parser.add_argument(
        '-e',
        '--envs',
        default='aws,hp,azure,joyent',
        help='A comma separated list of environments to test. Valid values'
             ' are "aws" (Amazon), "azure" (Azure), "hp" (HP public cloud)'
             ' "joyent" (Joyent), and "lxc" (Linux containers). Defaults to'
             ' "aws,azure,hp,joyent".',
    )
    parser.add_argument(
        '-j',
        '--job',
        default='',
        help='The value to use for the jenkins job ID. Set in the testing'
             ' environment as JOB_ID. Default is empty string.',
    )
    parser.add_argument(
        'url',
        help='The charm or bundle url to test, typically in the form'
             ' cs:precise/pictor-1 or gh:whitmo/bundle-kubernetes '
             ' Any bundletester-compatible url will work.',
    )
