import git,os
import shutil
import sys
import yaml
from os.path import isfile
from git import Repo
from flask import Flask


app = Flask(__name__)

DIR_NAME = "./config_repo73"
REMOTE_URL = str(sys.argv[1])

def pullgit_repo():
 if (os.path.isdir(DIR_NAME)):
  shutil.rmtree(DIR_NAME)
 os.mkdir(DIR_NAME)
 repo = git.Repo.init(DIR_NAME)
 origin = repo.create_remote('origin',REMOTE_URL)
 origin.fetch()
 origin.pull(origin.refs[0].remote_head)
 print "Showing files present in github repository:"
 print "Please browse the file which you want to display contents:"
 dirs = os.listdir(DIR_NAME)
 for file in dirs:
  print file
 print "---- END ----"


@app.route("/v1/<filename>")
def displayfilecontent(filename):
 extensions = '.yml','json'
 if filename.endswith(extensions):
   filepath= DIR_NAME +"/"+ str(filename)
   if isfile(filepath):
    with open(filepath, "r") as stream:
     docs = yaml.load_all(stream)
     for doc in docs:
      output=[]
      for k,v in doc.items():
        output.append(v)
      return "<br/>".join(output)
    stream.close()
   else:
    return "Page not found"
 else:
   return "file cannot open! No access rights"


if __name__ == "__main__":
    pullgit_repo()
    app.run(debug=True,host='0.0.0.0')