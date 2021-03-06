# Get Project's assets list
def get_prj_ast( fname ):
    import json
    from subprocess import PIPE, Popen

    # Enables the cloud resource manager API
    stdout, stderr = Popen("gcloud services enable cloudasset.googleapis.com",
                           shell=True, stdout=PIPE, stderr=PIPE).communicate()
    msg = (stderr + stdout).decode(encoding="utf-8")
    if ("ERROR" in msg):
        print( "Error Msg1: ", msg)
        return msg

    # Enables the cloud resource manager API
    stdout, stderr = Popen("gcloud beta asset search-all-resources --page-size=999999999 --format=json > {}".format(fname),
                           shell=True, stdout=PIPE, stderr=PIPE).communicate()
    msg = (stderr + stdout).decode(encoding="utf-8")
    if ("ERROR" in msg):
        print( "Error Msg2: ", msg)
        return msg

    # Test loading the JSON contents from the file
    with open( fname ) as file:
      rsc_json = json.load( file )

    return rsc_json
