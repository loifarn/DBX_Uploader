import sys
import os
from configparser import ConfigParser
from dropbox import Dropbox


class Uploader():
    def __init__(self):
        self.config = ConfigParser()
        self.initialize_dropbox()
        try:
            self.upload(sys.argv[1], sys.argv[2]) 
        except IndexError:
            print('Please add arguments \'localpath\' \'uploadpath\' ')

    def initialize_dropbox(self):
        try:
            self.config.read('{}/config.ini'.format(os.path.dirname(os.path.realpath(__file__))))
        except KeyError:
            print('Error. Could not find or access config.ini in app root directory')
            exit()

        try:
            self.token = self.config.get('DEFAULT', 'TOKEN')
        except KeyError:
            print('Error. Could load token from config.ini')
            exit()

        self.dropbox = Dropbox(self.token)

    def upload(self, file_path, dest_path):
        with open(file_path, 'rb') as file:
            self.dropbox.files_upload(file.read(), dest_path, mute=True)
        print('Uploaded {} to {} sucessfully'.format(file_path, dest_path))


if __name__ == '__main__':
    app = Uploader()
