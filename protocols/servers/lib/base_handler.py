import os
import time
from BaseHTTPServer import BaseHTTPRequestHandler


class GetHandler(BaseHTTPRequestHandler):
    # Some of the http server code came from Dave Kennedy's AES shell
    # over http - the server specific code

    # should be performing GET requests Help from
    # http://pymotw.com/2/BaseHTTPServer/
    def do_GET(self):

        # 404 since we aren't serving up any pages, only receiving data
        self.send_response(404)
        self.end_headers()
        return

    # handle post request
    def do_POST(self):

        # Gather the Posted URI from the agent/browser
        # parsed_path = urlparse.urlparse(self.path)
        uri_posted = self.path
        uri_posted = uri_posted.replace("/", "")
        #incoming_ip = self.client_address[0]
        # current directory
        exfil_directory = os.path.join(os.getcwd(), "data")
        loot_path = exfil_directory + "/"

        # Info for this from -
        # http://stackoverflow.com/questions/13146064/simple-
        # python-webserver-to-save-file
        if uri_posted == "ccdata.php":

            self.send_response(200)
            self.end_headers()
            loot_path = exfil_directory + "/"

            # Check to make sure the agent directory exists, and a loot
            # directory for the agent.  If not, make them
            if not os.path.isdir(loot_path):
                os.makedirs(loot_path)

            # Get the date info
            current_date = time.strftime("%m/%d/%Y")
            current_time = time.strftime("%H:%M:%S")
            screenshot_name = current_date.replace("/", "") +\
                "_" + current_time.replace(":", "") + "ccdata.txt"

            # Read the length of the screenshot file being uploaded
            screen_length = self.headers['content-length']
            screen_data = self.rfile.read(int(screen_length))

            # Write out the file
            with open(loot_path + screenshot_name, 'w') as cc_data_file:
                cc_data_file.write(screen_data)

        elif uri_posted == "ssndata.php":
            self.send_response(200)
            self.end_headers()

            # Check to make sure the agent directory exists, and a loot
            # directory for the agent.  If not, make them
            if not os.path.isdir(loot_path):
                os.makedirs(loot_path)

            # Get the date info
            current_date = time.strftime("%m/%d/%Y")
            current_time = time.strftime("%H:%M:%S")
            screenshot_name = current_date.replace("/", "") +\
                "_" + current_time.replace(":", "") + "ssndata.txt"

            # Read the length of the screenshot file being uploaded
            screen_length = self.headers['content-length']
            screen_data = self.rfile.read(int(screen_length))

            # Write out the file
            with open(loot_path + screenshot_name, 'w') as cc_data_file:
                cc_data_file.write(screen_data)

        # All other Post requests
        else:

            self.send_response(404)
            self.end_headers()

            print "Odd... someone else is trying to access this web server..."
            print "Might want to check that out..."
        return