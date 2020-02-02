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

from time import sleep
# Functions importing
from Image_comparison import compare_images
import Image_fetch

def compare_images_loop():
    '''
    It checks wheter the file inserted is valid, and returns True if
    it is valid, False otherwise

    return -- boolean
    '''

    file_to_check = input('\
            \nPlease insert the absolute path of the image to check. Only\
            \n.png, .jpg and .jpeg are accepted. Alternatively ou can also\
            \ndrag the file and drop it in this window\
            \n>> ')

    try:
        compare_images(file_to_check)
        return True
    except (IOError, FileNotFoundError):
        print('\nThe file does not exists, please select a different file')
        return False

# Main execution
print('\
    \nWelcome to the InstagramDuplicatesBot\
    \n-------------------------------------\
    \n(c) 2020 ERC Apps\n''')

if not Image_fetch.check_if_registered():
    Image_fetch.register_new_user()

try:
    Image_fetch.login_to_instagram()

    while True:
        if compare_images_loop():
            break
        else:
            continue
except:
    print('\
    \nSomething went wrong, if you have 2FA enabled make sure to uncomment and comment\
    \nthe appropriate lines of code in Scripts/Image_fetch.py')
