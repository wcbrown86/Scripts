"""
    
"""
import subprocess


class Terminal:

    def __init__(self):
        print("Start Terminal")

    # This function pulls the contents of the clip boards and translates that to a string then
    # returns that string.
    @staticmethod
    def pull_from_clipboard():
        return subprocess.check_output('pbpaste', env={'LANG': 'en_US.UTF-8'}).decode('utf-8')

    # This function puts the information back into the clipboard for the user to use as needed.
    @staticmethod
    def push_to_clipboard(contents):
        paste = subprocess.Popen('pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
        paste.communicate(contents.encode('utf-8'))




