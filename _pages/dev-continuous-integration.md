---
layout: default
title: Continuous Integration
category: Developer Docs
permalink: /dev/continuous-integration.html
---

# Continuous Integration

Juju can orchestrate deployments on many different cloud environments and has
an automated testing infrastructure that can test the same 
[charm]({{site.url}}/user/glossary.html#charm) 
or [bundle]({{site.url}}/user/glossary.html#bundle) on different deployment 
environments. 

The cloud environments included in the Juju testing infrastrure:
- [Amazon Web Services (AWS)](http://aws.amazon.com/)
- [HP Public cloud](http://www.hpcloud.com) (or any OpenStack cloud)
- [Microsoft Azure](http://azure.microsoft.com)
- [Joyent Compute Service](http://www.joyent.com/public-cloud)
- More to come soon!

## Kubenetes

The Kubernetes project test results can be viewed on 
[our result site](http://reports.vapour.ws/charm-summary/kubernetes).

This page shows the the Kubernetes release being tested and the 
status of the bundle tests on the different cloud environments as a pass or 
fail.

### Result Tests

Pass or Fail results are determined by the tests included with the kubernetes 
bundle.  We use a testing harness called 
[Amulet](https://juju.ubuntu.com/docs/tools-amulet.html) to drive 
integration tests and make assertions about the service(s) under load.

Good tests shoudl evalute the following:

 - Does the solution stand up (install and configure) properly?
 - Does the service respond to a workload?
   - Can we deploy a reference workload into kubernetes?
 - Does the service scale up and down?
   - Can we add units?
   - Can we remove units?

## How can I get involved?

We are not Kubneretes experts. Our current tests may not be the best way to 
test/stress a Kubernetes cluster. If you have some ideas for better tests we
would love to hear from you!  Please contribute an
[issue](http://github.com/{{site.repository}}/issues) or check
out our [contributing guide](contributing.html).


