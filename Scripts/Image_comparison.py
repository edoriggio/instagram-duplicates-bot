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

import cv2
from PIL import Image, ImageDraw

def compare_images(template: str, image: str = 'Assets/screenshot.png'):
    '''
    Given a template image and a profile page screenshot, the function checks
    whether the template is contained inside the screenshot. It also saves the
    marked image in the Assests folder as a png file

    template -- string
    image -- string
    '''

    print('\nInitiating image comparison\
        \n---------------------------')

    print('Resizing image')

    if Image.open(template).size == (293, 293):
        new_image = Image.open(template)
        resized = new_image.resize((293, 293))
        resized.save(template)

    im = cv2.imread(image)
    tmp = cv2.imread(template)

    template_size = tmp.shape[:2]

    result = cv2.matchTemplate(im, tmp, cv2.TM_SQDIFF)
    min_val, max_val, min_loc = cv2.minMaxLoc(result)

    confidence = (9999999999 - min_val) / 100000000
    altconfidence = 100 - ((min_val / max_val)*100)

    topleftx = min_loc[0]
    toplefty = min_loc[1]
    sizex = template_size[1]
    sizey = template_size[0]

    print('Comparing the images')

    if (altconfidence > 99) or ((confidence > 97) and (altconfidence > 93))\ or ((confidence > 95.7) and (altconfidence > 96.3)):
        marked = Image.open(image)
        draw = ImageDraw.Draw(marked)
        draw.line(((topleftx, toplefty), (topleftx + sizex, toplefty)), fill="red", width=2)
        draw.line(((topleftx + sizex, toplefty), (topleftx + sizex, toplefty + sizey)), fill="red", width=2)
        draw.line(((topleftx + sizex, toplefty + sizey), (topleftx, toplefty + sizey)), fill="red", width=2)
        draw.line(((topleftx, toplefty + sizey), (topleftx, toplefty)), fill="red", width=2)
        marked.save('Assets/screen_marked.png', "PNG")
        print('Potential duplicate was found, marked file saved in Assests/screen_marked.png\n')
    else:
        print ('No potential duplicates found\n')