# How to use this bundle

You have downloaded this bundle and are thinking to yourself:

*How do I get started?*

At a high level you will need to install Juju, enter your cloud credentials,
and deploy the kubernetes bundle.  This example is going to use an Ubuntu
system and the Amazon cloud environment, but the concepts are exactly the same
for other cloud environments.

# Install

You will need to [install the Juju client](https://juju.ubuntu.com/install) on
your local system type the following in a terminal:

    sudo add-apt-repository ppa:juju/stable
    sudo apt-get update
    sudo apt-get install juju-core juju-quickstart

## Configure the system for Amazon Web Services (AWS)

This process requires that you have an Amazon Web Services account.  You will
to provide your AWS credentials so Juju can manage your services on AWS for you.

    juju quickstart

This will give you an ncurses interface.

- Select `new Amazon EC2 environment`
- Type "amazon" in the environment name field.
- Copy and paste your AWS access key.
- Copy and paste your secret key.
- Select the nearest region to your location.
- Make this the default environment.
- Select `save` to write the changes to your environments.yaml file.
