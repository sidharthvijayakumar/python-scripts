"""""
This script is useful if you would like to pull Bulk information on the Last Build time, status, url for a Multibranch jenkins 
pipeline.

Run
pip3 install requests
"""

import requests
#import json #use this if you want pretty_json
import datetime

username="admin"
password="admn"
base_url="http://localhost:8081/"

pipelines=[]

#Function which gets the list of Multi branch pipelines from Jenkins
def get_pipelines_list():
    """
    Fetches the list of multibranch pipelines from Jenkins and filters only those with 
    the appropriate class (`org.jenkinsci.plugins.workflow.multibranch.WorkflowMultiBranchProject`).
    """
    url= f"{base_url}/api/json?tree=jobs[name,url]"
    try:
        response = requests.get(url,auth=(username,password),timeout=10)
        response.raise_for_status()
        data=response.json()
        #pretty_json=json.dumps(x.json(),indent=4)
        #print(pretty_json) #prints data in json pretty which is a string
        global pipelines #invoke the pipeline list
        pipelines= [
            job["name"] for job in data["jobs"]
            if job["_class"] == "org.jenkinsci.plugins.workflow.multibranch.WorkflowMultiBranchProject"
            ]
        print("Fetched pipelines:", pipelines)
    except requests.exceptions.ConnectionError as e:
        print(f"Connection issue: {e}")
    except requests.exceptions.HTTPError as e:
        print(f"Some error occuered: {e}")

#Function which returns the last build time and checks only master/main branches 
def get_build_time():
    """
    Retrieves build information for the specified pipeline and filters only the 'main' 
    or 'master' branches. Prints human-readable build details.
    """
    url = f"{base_url}/job/{pipeline}/api/json?tree=jobs[name,lastBuild[number,timestamp,result,url]]"
    try:
        response= requests.get(url, auth=(username,password),timeout=10)
        response.raise_for_status()
        data= response.json()
        filtered_jobs=[
            job for job in data["jobs"]
            if job["name"] in ["main","master"]
        ]
        if filtered_jobs:
            print("**************************")
            print(f"Pipeline:{pipeline}")
            for job in filtered_jobs:
                print(f"Job name: {job['name']}")
                #Need to change the time stamp from ms to human readble format
                print(f"Last Build Date :{datetime.datetime.fromtimestamp(job['lastBuild']['timestamp']/1000.0)}")
                print(f"Last build reseult : {job['lastBuild']['result']}")
                print(f"Last build url : {job['lastBuild']['url']}")
        else:
            print("**************************")
            print(f"{pipeline} has no master/main branch.")

    except requests.exceptions.ConnectionError as e:
        print (f"Connection issues: {e}")
    except requests.exceptions.HTTPError as e:
        print(f"Some error occuered: {e}")

#Call the get list pipeline function to get latest list of pipelines
get_pipelines_list()

#Invoke the function to get the last build status
for pipeline in pipelines:
    get_build_time()
