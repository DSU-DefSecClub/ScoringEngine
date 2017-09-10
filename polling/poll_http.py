import requests
from requests.exceptions import *
import tempfile

from poller import PollInput, PollResult, Poller

class HttpPollInput(PollInput):

    def __init__(self, proto, path, server=None, port=None):
        super(HttpPollInput, self).__init__(server, port)
        self.proto = proto
        self.path = path

class HttpPollResult(PollResult):

    def __init__(self, file, exceptions):
        super(HttpPollResult, self).__init__(exceptions)
        self.file = file

class HttpPoller(Poller):
    
    def poll(self, poll_input):
        try:
            proto = poll_input.proto
            server = poll_input.server
            port = poll_input.port
            path = poll_input.path
            r = requests.get('{}://{}:{}/{}'.format(proto, server, port, path), timeout=2)
            r.raise_for_status()

            t = tempfile.TemporaryFile()
            t.write(r.text)

            result = HttpPollResult(t, None)
            return result
        except Exception as e:
            result = HttpPollResult(None, e)
            return result
