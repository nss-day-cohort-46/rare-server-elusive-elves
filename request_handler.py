import json
from http.server import BaseHTTPRequestHandler, HTTPServer

from users import get_all_users, get_single_user, check_user, create_user
from posts import get_all_posts, get_single_post, get_posts_by_user_id, create_post, delete_post, update_post, get_post_by_category
from comments import get_all_comments, get_single_comment, create_comment, delete_comment, update_comment


class HandleRequests(BaseHTTPRequestHandler):
    
    def parse_url(self, path):

        path_params = path.split("/") # localhost:8088/entries/1
        resource = path_params[1]

        if "?" in resource:
            
            param = resource.split("?")[1]
            resource = resource.split("?")[0]

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
        response = {}
        parsed = self.parse_url(self.path)
        
        #fetch with 2
        if len(parsed) == 2:
            (resource, id) = parsed

            if resource == 'login':
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
            
            # if resource == 'tags':
            #     if id is not None:
            #         response = f"{get_single_tag(id)}"
            #     else:
            #         response = f"{get_all_tags()}"
            
            # if resource == 'categories':
            #     if id is not None:
            #         response = f"{get_single_category(id)}"
            #     else:
            #         response = f"{get_all_categories()}"
            
            # if resource == 'reactions':
            #     if id is not None:
            #         response = f"{get_single_reaction(id)}"
            #     else:
            #         response = f"{get_all_reactions()}"
            
            # if resource == 'subscriptions':
            #     if id is not None:
            #         response = f"{get_single_subscription(id)}"
            #     else:
            #         response = f"{get_all_subscriptions()}"

            # for now
            pass

        
        
        #Fetch call with 3
        elif len(parsed) == 3:
            (resource, key, value) = parsed
            value = int(value)
            if resource == "posts" and key == "user":
                response = f"{get_posts_by_user_id(value)}"

            if resource == "posts" and key == "categories":
                response = f"{get_post_by_category(value)}"

        self.wfile.write(response.encode())



    def do_DELETE(self):
        self._set_headers(204)
        (resource, id) = self.parse_url(self.path)

        # if resource == "users":
        #     delete_user(id)


        if resource == "posts":
            delete_post(id)

        if resource == "comments":
            delete_comment(id)

        # if resource == "subscriptions":
        #     delete_subscription(id)
        # if resource == "reactions":
        #     delete_reaction(id)
        # if resource == "tags":
        #     delete_tag(id)
        # if resource == "categories":
        #     delete_category(id)

        self.wfile.write("".encode())
    
    def do_PUT(self):
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        (resource, id) = self.parse_url(self.path)

        success = False

        # if resource == "users":
        #     success = update_user(id, post_body)

        if resource == "posts":
            success = update_post(id, post_body)

        if resource == "comments":
            success = update_comment(id, post_body)

        # if resource == "subscriptions":
        #     success = update_subscription(id, post_body)
        # if resource == "reactions":
        #     success = update_reaction(id, post_body)
        # if resource == "tags":
        #     success = update_tag(id, post_body)
        # if resource == "categories":
        #     success = update_category(id, post_body)


        if success:
            self._set_headers(204)
        else:
            self._set_headers(404)
        
        self.wfile.write("".encode())
        

        
        



    def do_POST(self):

        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        
        post_body = json.loads(post_body)

        (resource, id) = self.parse_url(self.path)

        new_item = None

        if resource == "login":
            new_item = check_user(post_body)
        elif resource == "register":
            new_item = create_user(post_body)

        elif resource == "posts":
            new_item = create_post(post_body)
       
        elif resource == "comments":
            new_item = create_comment(post_body)

        # elif resource == "tags":
        #     new_item = create_tag(post_body)
        # elif resource == "reactions":
        #     new_item = create_reaction(post_body)
        # elif resource == "subscriptions":
        #     new_item = create_subscription(post_body)
        # elif resource == "categories":
        #     new_item = create_category(post_body)




        self.wfile.write(f"{new_item}".encode())


def main():

    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()

if __name__ == "__main__":
    main()

