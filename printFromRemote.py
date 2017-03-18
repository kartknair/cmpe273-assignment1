from github import Github
import sys
from flask import Flask

app = Flask(__name__)


@app.route("/v1/<filename>")
def printfrmremoteresource(filename):
    cmdlineargs = (sys.argv[1]).split("/")
    userID = cmdlineargs[3]
    repository = cmdlineargs[4]
    repo = Github().get_user(userID).get_repo(repository)
    extension = '.json', '.yml'
    out = []
    if (filename != None):
        if filename.endswith(extension):
            configfile = repo.get_contents(filename)
            out.append(configfile.decoded_content)
            return "<br/>".join(out)
        else:
            return "Incorrect file extension!"
    else:
        return "The requested url is unavailable, Page not found"


@app.route("/")
def hello():
    return "Hello from Dockerized Flask App!! "


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')