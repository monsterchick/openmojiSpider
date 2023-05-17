import os
import requests
import re
from create_folder_or_file import Create


class GetData:
    def __init__(self):
        self.create = Create()
        self.url = ''

    def get_response_text(self, url):
        response = requests.get(url)
        return response

    def mkfolder(self, f_name):
        self.f_name = f_name
        self.create.mkdir(folder_name=self.f_name)
        return f_name

    def download_image(self, img_url, img_name):
        # download images with svg format
        folder_path = self.mkfolder(self.f_name)
        print("downloading {img}...".format(img=img_name))
        response_image = requests.get(img_url)
        with open(os.path.join(folder_path, img_name), 'wb') as f:  # open the path of image file
            f.write(response_image.content)
        f.close()

    def get_data(self):
        text = self.get_response_text(url='https://openmoji.org/library/').text
        src_list = re.findall(r'<a class="emojiDetailsLink astro-JSGNIHCK" href=".*?">', text)

        for src in src_list:
            # get path of image
            src_clip = src.split("\"")[3].split("/")[2]
            # get main url
            main_page = 'https://openmoji.org/library/' + self.url + src_clip

            text = self.get_response_text(url=main_page).text
            img_src_list = re.findall(r'id="downloadPNG" href=".*?" download', text)

            for imgSrc in img_src_list:
                img_url = "https://openmoji.org/" + imgSrc.split('href="/')[1].split('\"')[0].replace("amp;", "")
                img_name = re.findall(r'<h1 class="astro-3TWLDLUD">.*?</h1>', text)[0].split(">")[1].split("<")[0] + "_" + img_url.split("=")[3] + ".png"
                self.download_image(img_url, img_name)

    def start(self):
        try:
            self.mkfolder('image')
            self.get_data()
        except KeyboardInterrupt:
            print('program exited!')


GetData().start()
