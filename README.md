
# Overview

This is a simple demo of using Cloud Foundry, Flask, Python 3, and TensorFlow.

## Requirements

- [ ] You must have at minimum a [Predix Free Tier](signup) account.
- [ ] You must have the [Cloud Foundry CLI](cf) and can run `cf login`

# Setup

```
git clone https://github.com/j12y/predix-tensorflow-example
cd predix-tensorflow-example
```

You'll want to change the application name to something unique just for you.

```
cf push --random-route
```

# Results

When you push the app you should see something like the following.

```
App predix-tensorflow-example was started using this command `python app.py`

Showing health and status for app predix-tensorflow-example in org
***************@**.com / space tensorflow as ***************@**.com...
OK

requested state: started
instances: 1/1
usage: 1G x 1 instances
urls: predix-tensorflow-example-subordinal-lid.run.aws-usw02-pr.ice.predix.io
last uploaded: Fri Sep 1 15:14:37 UTC 2017
stack: cflinuxfs2
buildpack: https://github.com/cloudfoundry/buildpack-python.git

     state     since                    cpu      memory         disk
details
#0   running   2017-09-01 08:16:52 AM   162.6%   251.9M of 1G   487.5M of 1G
```

You can add https:// to the url listed and see your simple tensorflow app
running.

# Description

This is the basic example from Getting Started with TensorFlow.  When combined
with the Predix SDK you can start pulling data from services like Predix Asset
and Predix Time Series.

For more information about the SDK see:

- https://github.com/PredixDev/predixpy

For more details on how Flask works, what runtime.txt, Procfiles, etc. are
about see the basic flask app repository:

- https://github.com/j12y/predix-py3-flask


---
[signup]: https://www.predix.io/registration
[cf]: https://github.com/cloudfoundry/cli
[buildpack]: http://docs.cloudfoundry.org/buildpacks/python/
