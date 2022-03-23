


import requests
from bs4 import BeautifulSoup


class WeatherApp:
    listNumber = {
    "เชียงราย":1, "เชียงใหม่":2, "น่าน":5, "พะเยา":11, "แพร่":14, "แม่ฮ่องสอน":3,"ลำปาง":13,"ลำพูน":12, "อุตรดิตถ์":6,"กาฬสินธุ์":28, 
    "ขอนแก่น":18, "ชัยภูมิ":29, "นครพนม":25, "นครราชสีมา":20, "บึงกาฬ":81, "บุรีรัมย์":33, "มหาสารคาม":27, "มุกดาหาร":22, "ยโสธร":31, 
    "ร้อยเอ็ด":21, "เลย":17, "สกลนคร":26, "สุรินทร์":32, "ศรีสะเกษ":30, "หนองคาย":16, "หนองบัวลำภู":24, "อุดรธานี":23, "อุบลราชธานี":19, 
    "อำนาจเจริญ":34,"กรุงเทพมหานคร":37,"กำแพงเพชร":8, "ชัยนาท":39, "นครนายก":60, "นครปฐม":50, "นครสวรรค์":36, "นนทบุรี":49, "ปทุมธานี":43, 
    "พระนครศรีอยุธยา":41, "พิจิตร":9, "พิษณุโลก":7, "เพชรบูรณ์":15, "ลพบุรี":40, "สมุทรปราการ":51, "สมุทรสงคราม":46, "สมุทรสาคร":52, "สิงห์บุรี":45, 
    "สุโขทัย":10, "สุพรรณบุรี":38, "สระบุรี":44, "อ่างทอง":47, "อุทัยธานี":48, "จันทบุรี":58,"ฉะเชิงเทรา":59,"ชลบุรี":61,"ตราด":57,"ปราจีนบุรี":56,
    "ระยอง":55,"สระแก้ว":53,"กาญจนบุรี":35,"ตาก":4,"ประจวบคีรีขันธ์":71,"เพชรบุรี":70,"ราชบุรี":42,"กระบี่":76,"ชุมพร":63,"ตรัง":77,
    "นครศรีธรรมราช":64,"นราธิวาส":65,"ปัตตานี":68,"พังงา":78,"พัทลุง":73,"ภูเก็ต":75,"ระนอง":74,"สตูล":79,"สงขลา":80,"สุราษฎร์ธานี":72,"ยะลา":67, 
    }
    
    def __init__(self):
        
        self.provinceNumber = ""

    def putprovince(self):
        province = str(input('enter your province weather\n'))
        self.provinceNumber = province
        return self.provinceNumber
        
    def showWeather(self):
        if  self.listNumber.get(self.provinceNumber) :
            url = f"https://www.tmd.go.th/province.php?id={self.listNumber[self.provinceNumber]}"

            r = requests.get(url)

            r.encoding
            soup =BeautifulSoup(r.text , 'html.parser')

            span = soup.find_all("td", {"class": "strokeme"})

            print(span)

            lists = []

            for list in span :
                lists.append(list.string)
            
            result = " ".join(lists)

            print(f"The weather today  {self.provinceNumber} is {result}")



        else:
            print('โปรด ใส่ จังหวัดที่ต้องการ ก่อนคาะ !!') 




be =WeatherApp()
be.putprovince()
be.showWeather()