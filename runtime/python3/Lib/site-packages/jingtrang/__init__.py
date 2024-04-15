import os
import subprocess
import sys

import pkg_resources

HERE = os.path.split(__file__)[0]
JING_JAR = os.path.join(HERE, "jing.jar")
TRANG_JAR = os.path.join(HERE, "trang.jar")


def jing():
    cmd = ["java", "-jar", JING_JAR]
    cmd = cmd + sys.argv[1:]
    res = subprocess.call(cmd, stdout=sys.stdout, stderr=sys.stderr, stdin=sys.stdin)
    sys.exit(res)


def trang():
    cmd = ["java", "-jar", TRANG_JAR]
    cmd = cmd + sys.argv[1:]
    res = subprocess.call(cmd, stdout=sys.stdout, stderr=sys.stderr, stdin=sys.stdin)
    sys.exit(res)
