#!/usr/bin/env python
# Import libraries
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler   # Needed for http server
from SocketServer import ThreadingMixIn                         # Needed for multi-threading
import urlparse                                                 # Needed to get data from http request
from neopixel import *                                          # Needed to control the leds    

strip = Adafruit_NeoPixel(num = 60, pin = 18)               # num is the number of leds
strip.begin()                                               # Start leds

def set_all_pixels(r=0, g=0, b=0):                          # Changes all leds to the same color
    for i in range(strip.numPixels()):                      # Loop through all leds
        strip.setPixelColor(i, Color(int(g),int(r),int(b)))                # Set each led
    strip.show()                                            # Send updated colors to the leds

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):                                       # Handles the http GET request
        self.send_response(200)                             # Sends a "OK" response
        self.send_header('Access-Control-Allow-Origin','*') # Sends a special header that allows ajax from another server 
        self.end_headers()                                  # End header
        
        o = urlparse.urlparse(self.path)                    # Create a url parser from the request
        query = urlparse.parse_qs(o.query)                  # Parse the request url
        
        if 'red' in query and 'green' in query and 'blue' in query: # Check that the request has red green and blue
            set_all_pixels(query['red'][0], query['green'][0], query['blue'][0]) # Send color data to set_all_pixels function 
        return

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    pass

if __name__ == '__main__':
    httpd = ThreadedHTTPServer(('0.0.0.0', 8080), Handler) # Create a multi-threaded http server on port 8080
    print('Starting server, use <Ctrl-C> to stop')          # Print a mesage to the console
    httpd.serve_forever()                                  # Start server
