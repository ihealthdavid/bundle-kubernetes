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

## Configure Juju to use Amazon Web Services (AWS)

This process requires that you have an Amazon Web Services account.  You will
to provide your AWS credentials so Juju can manage your services on AWS for you.

    juju quickstart https://raw.githubusercontent.com/whitmo/bundle-kubernetes/master/bundles.yaml

Select `new Amazon EC2 environment` from the ncurses interface and fill in the
following fields:  

- Type "amazon" in the environment name field.
- Copy and paste your AWS access key.
- Copy and paste your AWS secret key.
- The 'admin secret' is the password you will use to log in to the Juju GUI.
- Make this the default environment.
- Select `save` and `use` to write the changes to your environments.yaml file.

The Juju client using Secure Shell (SSH) to intereact with the servers in the
cloud.  Quickstart will prompt you to create SSH keys if you do not already
have keys on this system.

The bootstrap process will create a virtual machine that Juju will use for
orchestration.  Quickstart will also deploy the Juju Graphical User Interface
(GUI) to the bootstrap node.

If your system is configured with a default browser, Quickstart will open it to
the Juju GUI.  Since the certificate is self signed you may need to add an
exception for the certificate in the browser.  Quickstart will log you in to
the Juju GUI presenting you with a welcome screen, click the "Get started"
button to dismiss the dialog.

You will see the Kubernetes charms on the Juju GUI. The VMs are booting,
installing software and creating relations between systems.  This may take a
few minutes to get the full environment stood up.

## Start using Kubernetes

Now that you have Kubernetes fully deployed, you can ssh to the
kubernetes-master unit and use the kubectl command to interact with the system.

    juju ssh kuberenetes-master/0

You can follow the
(GuestBook)[https://github.com/GoogleCloudPlatform/kubernetes/blob/master/examples/guestbook/README.md]
example application instructions.  Please note that the Kubernetes software
has been installed in the '/opt/kubernetes' directory.

The example application calls for using the `gcloud` tool to open ports.  In
this case we will use Juju to open the any ports needed.

For example, if there is a need to open firewall port 8000 on the Kuberentes
minions use `juju run` to accomplish the same outcome:

    juju run --services kubernetes 'open-port 8000'
