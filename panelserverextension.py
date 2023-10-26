from subprocess import Popen


def load_jupyter_server_extension(nbapp):
    Popen(["panel", "serve", "run.py", "--allow-websocket-origin=*"])
