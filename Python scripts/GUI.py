# Copyright  2020  Edoardo Riggio
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import tkinter as tk
import json

json_file = 'Json/credentials.json'

class MainApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_columnconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        self.frames = {}

        for page in (Login, Home, Result):
            frame = page
            self.frames[page] = frame
            # frame.grid()

        def show_frame(self, container):
            frame = self.frames[container]
            frame.tkraise()

        json_data = read_write_to_json(json_file)

        if json_data['username'] == '' or json_data['password'] == '':
            show_frame(Login())
        else:
            show_frame(Home())

class Login(tk.Tk):
    pass

class Home(tk.Tk):
    pass

class Result(tk.Tk):
    pass

# Function for reading and writing data froma a JSON file
def read_write_to_json(file: str, data: dict = {}, readwrite: str = 'r'):
    if readwrite == 'r':
        with open(file, 'r') as file_to_read:
            return json.load(file_to_read)
    elif readwrite == 'w':
        with open(file, 'w') as file_to_write:
            json.dump(data, file_to_write)
    else:
        raise Exception("readwrite must be either 'r' or 'w'")

app = MainApp()
app.mainloop()