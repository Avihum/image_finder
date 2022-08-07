from dataclasses import dataclass
# import PIL.Image as Image
from typing import Dict, Any

import requests


@dataclass
class img_finder:
    __codes_bytes_dict = {}

    def find(self, error_code: int) -> bytes:
        bytes_to_return: bytes
        if type(error_code) is not int:
            raise TypeError("only integers are allowed")  # I can also just return None and write the reason somewhere
        if error_code not in self.__codes_bytes_dict:
            try:
                response = requests.get(f'https://http.dog/{error_code}.jpg')
            except Exception as e:
                print(e)
                return None
            if (response.status_code / 100) == 2:
                self.__codes_bytes_dict[error_code] = response.content
                # img = Image.open(BytesIO(response.content))
                # img.show()
            else:
                self.__codes_bytes_dict[error_code] = None
        return self.__codes_bytes_dict[error_code]
