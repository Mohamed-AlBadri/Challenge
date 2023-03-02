# To query the metadata of a Google Cloud Platform (GCP) instance 
# and provide a JSON formatted output using Python, we can use the google.auth 
# and google.auth.compute_engine modules to obtain credentials for the instance, 
# and the googleapiclient module to make API requests to the Metadata Server.


import json
from google.auth import compute_engine
from googleapiclient import discovery

# Create a client object to access the Metadata Server
credentials = compute_engine.Credentials()
service = discovery.build('compute', 'v1', credentials=credentials)

# Query the instance's metadata
project = service.projects().get(project='project-id').execute()
zone = 'zone-name'
name = 'instance-name'
instance = service.instances().get(project=project['projectId'], zone=zone, instance=name).execute()

# Print the metadata in JSON format
print(json.dumps(instance, indent=2))

# hint
# Replace 'project-id', 'zone-name', and 'instance-name' with the values for your GCP instance.
# The json.dumps function with indent=2 parameter is used to pretty-print the JSON output.

# The google-auth and google-auth-compute-engine modules are included in the google-auth package,
#  which you can install using pip:

# pip install google-auth

# The googleapiclient module is included in the google-api-python-client package,
#  which you can install using pip:

# pip install google-api-python-client


# Before running the code, make sure that the instance has the appropriate scopes to access the Metadata
# Server. If you're using the default service account for the instance,
# it should have the https://www.googleapis.com/auth/cloud-platform scope,
# which provides full access to all Google Cloud APIs, including the Metadata Server.