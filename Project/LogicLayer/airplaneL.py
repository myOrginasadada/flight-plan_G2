#from import
#from import

class AirplaneL:
    def __init__(self, data_wrapper):
        self.data_wrapper = data_wrapper

    def register_airplane(self, airplane_info):
        self.data_wrapper.create_airplane(airplane_info)

    def edit_airplane_info(self, airplane_name, update_info):
        if not self.data_wrapper.get_airplane(airplane_name):
            return False
        return self.data_wrapper.edit_airplane(airplane_name, update_info)

    def get_plane_info(self, airplane_name):
        return self.airplanes.get_airplane(airplane_name)