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

Select `new Amazon EC2 environment` from the ncurses interface and fill in the
following fields:  

- Type "amazon" in the environment name field.
- Copy and paste your AWS access key.
- Copy and paste your AWS secret key.
- Optional select the nearest region to your location.
- The 'admin secret' is the password you will use to log in to the Juju GUI.
- Make this the default environment.
- Select `save` and `use` to write the changes to your environments.yaml file.

Quickstart will start a node using your Amazon credentials for the bootstrap
node.  
