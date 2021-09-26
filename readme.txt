DEVELOPMENT

prerequirements 
1.ติดตั้ง python 3.6 ขึ้นไป
2.ติดตั้ง pip
3.ติดตั้ง flask
// การติดตั้ง flask อาจจะไม่ได้ติดบางแพ็คเกจมาให้ เช่น Blueprint ซึ่งอาจต้องติดตั้งอีกทีแนะนำใช้ pip


วิธีรัน :
1.เปิด Terminal (รันใน path > webstream/app)
2.พิมพ์ python app.py
//

API
1.write customer table 
2.read customer table
3.


DEPLOYMENT ( การทำ Image เพื่ออัพโหลดขึ้น Cloud )

Docker :
image name : softent1

command :
1. docker built -t softent1 .
2. docker run -d --restart=always -p 80:80 -t softent1


Version Controll ( การอัพเดทงานขึ้น Github )

1.git init

2.git commit -m "Your comment"
Ex. git commit -m "add auth.py"

3.git remote add origin <Link to GitHub Repo>

4.git push -u origin master 