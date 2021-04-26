import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class HandleRequests(BaseHTTPRequestHandler):
    
    def parse_url(self, path):

        path_params = path.split("/") # localhost:8088/entries/1
        resource = path_params[1]

        if "?" in resource:

            resource = resource.split("?")[0]
            param = resource.split("?")[1]

            pair = param.split("=")

            key = pair[0]
            value = pair[1]

            return (resource, key, value)

        else:

            id = None
            try:

                id = int(path_params[2])
            except IndexError:
                pass
            except ValueError:
                pass

            return (resource, id)

    
    
    def _set_headers(self, status):

        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    
    
    def do_OPTIONS(self):

        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    

    def do_GET(self):
        self._set_headers(200)
        response = []

        parsed = self.parse_url(self.path)
        
        if len(parsed) == 2:
            (resource, id) = parsed

        elif len(parsed) == 3:
            (resource, key, value) = parsed


    def do_DELETE(self):
        self._set_headers(204)
        (resource, id) = self.parse_url(self.path)


    
    def do_PUT(self):
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        (resource, id) = self.parse_url(self.path)

        success = False

        if resource == 'users':
            if id is not None:
                response = f"{get_single_user(id)}"
            else:
                response = f"{get_all_users()}"
        
        if resource == 'posts':
            if id is not None:
                response = f"{get_single_post(id)}"
            else:
                response = f"{get_all_posts()}"
        
        if resource == 'comments':
            if id is not None:
                response = f"{get_single_comment(id)}"
            else:
                response = f"{get_all_comments()}"
        
        if resource == 'tags':
            if id is not None:
                response = f"{get_single_tag(id)}"
            else:
                response = f"{get_all_tags()}"
        
        if resource == 'categories':
            if id is not None:
                response = f"{get_single_category(id)}"
            else:
                response = f"{get_all_categories()}"
        
        if resource == 'reactions':
            if id is not None:
                response = f"{get_single_reaction(id)}"
            else:
                response = f"{get_all_reactions()}"
        
        if resource == 'subscriptions':
            if id is not None:
                response = f"{get_single_subscription(id)}"
            else:
                response = f"{get_all_subscriptions()}"

        
        



    def do_POST(self):




def main():

    host = ''
    port: 8088
    HTTPServer((host, port), HandleRequests).serve_forever()

if __name__ == "__main__":
    main()

