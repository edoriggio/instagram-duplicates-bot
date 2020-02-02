# InstagramDuplicates

## Short description
This script logs into a user's Instagram account and checks if, given an image, this is already present in the user's profile page (i.e. the photo is a duplicate).

**Python version - 3.6.9**

## Packages used
- opencv-python
- Pillow
- Selenium

Install these packages in order to make the script work correctly. This can be done using the following command

```bash
pip3 install opencv-python Pillow Selenium
```

## Installing Selenium driver for Firefox
1. Go to [this website][1] and look for the driver for your OS.
2. Go to the directory where the driver was installed to and unzip the archive
3. Open the Terminal and write (write the path insted of the line of text between the parenteses, and the parenteses too)
```
sudo mv (relative path of the installed driver) /usr/local/bin
```
After inserting your password, this will make sure that the driver is moved to the right directory, so that the script will work correctly.

## How does it work
The script runs in the terminal. And operates in the following order
1. It asks the user (if he/she uses the script for the first time) their Instagram username and password, which will then be saved in a json file for further reference;
2. It tries to log in the given user Instagram account using Selenium and the Firefox driver (so make sure to have installed it beforehand)
    - If the 2FA is off or the script is not running for the first time, selenium will be used to log in the user's account and take a fullpage screenshot of the profile page (n.b. this only works when the 'headless' mode is turned on)
    - If the 2FA is on or in general during the first run, it is necessary to run the script with a visible firefox window. This can be done by changing the lines in [Image_fetch.py][2].

```python
driver = webdriver.Firefox(options = op)  #comment it out
# driver = webdriver.Firefox()            #uncomment it
```

3. The script will then promt the user to input the absolute path of the image they want to check. This can be done in two ways, either by writing down the absolute path of the file, or by dragging and dropping the desired file into the Terminal window
4. An image recognition script will begin to run and it will check if the given image is inside the screenshot that was previously taken. The script will then save a .png in the [Assets][3] folder containing the screenshot taken earlier and a red square if the image was found.

[1]: https://github.com/mozilla/geckodriver/releases
[2]: Scripts/Image_fetch.py
[3]: Assets
