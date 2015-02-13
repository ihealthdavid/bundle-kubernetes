---
layout: default
title: Getting Started
category: User Docs
permalink: /user/getting-started.html
---

# How to use this bundle

You have downloaded this bundle and are thinking to yourself: *How do
I get started?*

You will need to install Juju, enter your cloud credentials, and
deploy the kubernetes bundle.  This example will assume the use of an
Ubuntu system and the Amazon cloud environment, but the concepts are
the same for other cloud environments.

# Install Juju

You will need to
[install the Juju client](https://juju.ubuntu.com/install) on your
local system type the following in a terminal:

    sudo add-apt-repository ppa:juju/stable
    sudo apt-get update
    sudo apt-get install juju-core juju-quickstart

## Configure Juju to use Amazon Web Services (AWS)

This process requires that you have an Amazon Web Services account.
You will to provide your AWS credentials so Juju can manage your
services on AWS for you.

    juju quickstart https://raw.githubusercontent.com/whitmo/{{ site.repository }}/master/bundles.yaml

Select `new Amazon EC2 environment` from the ncurses interface and
fill in the following fields:

- Type "amazon" in the environment name field.
- The 'admin secret' is the password you will use to log in to the
  Juju GUI.

![juju quickstart1]({{site.url}}/images/quickstart1.png)

- Copy and paste your AWS access key.
- Copy and paste your AWS secret key.

![juju quickstart2]({{site.url}}/images/quickstart2.png)

- Make this the default environment.
- Select `save` and `use` to write the changes to your
  environments.yaml file.

![juju quickstart3]({{site.url}}/images/quickstart3.png)

The Juju client using Secure Shell (SSH) to intereact with the servers
in the cloud.  Quickstart will prompt you to create SSH keys if you do
not already have keys on this system.

The bootstrap process creates a virtual machine that Juju will use
for orchestration.  Quickstart will also deploy the Juju Graphical
User Interface (GUI) to the bootstrap node.

If your system is configured with a default browser, Quickstart will
open it to the Juju GUI.  Since the certificate is self signed you may
need to add an exception for the certificate in the browser.
Quickstart will log you in to the Juju GUI presenting you with a
welcome screen, click the "Get started" button to dismiss the dialog.

You will see the Kubernetes charms on the Juju GUI. The VMs are
booting, installing software and creating relations between systems.
This may take a few minutes to get the full environment stood up.
Deployment on AWS generally takes about 300 - 400 seconds on AWS.

![juju gui]({{site.url}}/images/kubernetes-bundle-juju-gui.png)

## Start using Kubernetes

Now that Kubernetes fully deployed, you can follow the
[GuestBook example](user-guestbook-how-to.html) instructions that start an
application in Kubernetes. Juju has done the work of provisioning the
virtual machines, and the charms install and configure the Kubernetes
software.  You should be able to run through the Guestbook example and
get a working application.

![kubernetes guestbook example]({{site.url}}/images/guestbook.png)

# Destroy environment

Once you are done using Kubernetes on the cloud use Juju to stop
the servers.

    juju destroy-environment amazon

This command will terminate the virtual machines cloud that are running
Kubernetes, including the machine used for the Juju bootstrap node.
