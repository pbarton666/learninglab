#py_trigger_server_1.py

'''Run a local cgi server from the current directory that treats *.cgi files
as executable python cgi scripts.'''

#
from  http.server import HTTPServer, CGIHTTPRequestHandler
import sys, os

class CGIExtHTTPRequestHandler(CGIHTTPRequestHandler):
    '''This request handler looks for CGI filesto end in '.cgi' and 
    be in any directory as opposed to the CGIHTTPServer
    expectation that the cgi script are of the form /cgi-bin/*.py.'''
    
    def is_python(self, path):
        """Test whether argument path is a Python script: allow .cgi"""
        return path.lower().endswith('.cgi')

    def is_cgi(self):
        '''As on xenon, go by extension only.'''
        base = self.path
        query = ''
        i = base.find('?')
        if i != -1:
            query = base[i:]
            base = base[:i]
        if not base.lower().endswith('.cgi'):
            return False
        [parentDirs, script] = base.rsplit('/', 1)
        self.cgi_info = (parentDirs, script+query)
        return True
   

def run_server():
    dirName = os.getcwd()
    blanks = dirName.count(' ')
    if 0 < blanks:  # server cannot handle blanks in path names
        print ("The path to {} contains space(s):".format(blanks))
        print ("Either rename {} to remove the blanks or move it")
        return
        
    server_addr = ('localhost', 8000)
    cgiServer = HTTPServer(server_addr, CGIExtHTTPRequestHandler)
    sys.stderr.write('Localhost CGI server started\n.')
    cgiServer.serve_forever()

run_server()