#!/usr/bin/python

from startbloggerPost.template import tempstr
import datetime
import os
import subprocess

if __name__ == "__main__":
    now = datetime.datetime.now()
    tempfile = "htmltemp_%02d%02d_%02d%02d_%02d.html" % (
        now.month, now.day, now.hour,
        now.minute, now.second
        )
    temppath = os.path.join("/tmp", tempfile)
    print(temppath)

    with open(temppath, "w") as fh:
        fh.write(tempstr)

    subprocess.Popen(["gvim", "+/htmlstarthere", temppath])
    subprocess.Popen(["firefox", temppath])
