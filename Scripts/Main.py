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

from Image_comparison import compare_images
from Image_fetch import login_to_instagram

print('''
Welcome to the InstagramDuplicatesBot
-------------------------------------
(c) 2020 ERC Apps ''')

file_to_check = input('''
Please insert the absolute path of the image to check. Only
.png, .jpg and .jpeg are accepted
>> ''')

try:
    compare_images(file_to_check)
except (IOError, FileNotFoundError):
    print('\nThe file does not exists, please select another file')



# try:
#     login_to_instagram()
# except:
#     print('''
#     Something went wrong, if you have 2FA enabled make sure to uncomment and comment
#     the appropriate lines of code in Scripts/Image_fetch.py
#     ''')
