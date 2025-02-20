import base64
import xml.etree.ElementTree as ET
import os

class BurpReader():
    def __init__(self, file_path):
        self.file_path = file_path

        self.raw_requests = []
    
    def open_file(path):
        if os.path.isfile(path):
                with open(path, "r", encoding="utf-8") as f:
                    xml_content = f.read()
                return xml_content
        else:
                print("[X] File does not exists!")
                return None
        
    def parse_requests(self, file_path=None):
        if file_path:
            self.file_path = file_path
            xml_content = self.open_file(file_path)
        else:
            xml_content = self.open_file(file_path)


        # XML parszolása
        root = ET.fromstring(xml_content)

        # Csak a RAW HTTP requesteket gyűjtjük egy listába
        self.raw_requests = [
            base64.b64decode(item.find("request").text).decode(errors="ignore")
            for item in root.findall(".//item")
            if item.find("request") is not None
        ]


    def get_raw_requests(self):
        return self.raw_requests
