import requests
from requests.structures import CaseInsensitiveDict

mail = "mail@gmail.com"
drivename = "Name of the drive"

url = "https://team.gdrive.vip/drive"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Content-Type"] = "application/json"

data = "{\"teamDriveName\":\"" + drivename + "\",\"teamDriveThemeId\":\"random\",\"emailAddress\":\"" + mail + "\"}"

resp = requests.post(url, headers=headers, data=data)

print(resp.status_code)