
class ManipulandoJson:

    def get_username(self, json):
        return json["username"]
    
    def get_password(self, json):
        return json["password"]
    
    def get_host(self, json):
        return json["host"]
    
    def get_port(self, json):
        return json["port"]
    
    def get_device_type(self, json):
        return json["device_type"]
    
    def get_device_id(self, json):
        return json["device_id"]
    
    def get_sufix_result(self, json):
        return json["sufix_result"]
    
    def get_routing_key(self, json):
        return json["routing_key"]
    def get_process(self, json):
        return json["process"]
    
    def get_bundbox(self, json):
        json_bundbox = json["process"]
        return json_bundbox['bundbox']
    
    def get_rotation(self, json):
        json_rotation = json["process"]
        return json_rotation["rotation"]
    
 
    
    