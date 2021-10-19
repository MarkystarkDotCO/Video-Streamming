@DEVELOPMENT

Pre requirements 
1.ติดตั้ง python 3.6 ขึ้นไป
2.ติดตั้ง pip
3.ติดตั้ง flask
// การติดตั้ง flask อาจจะไม่ได้ติดบางแพ็คเกจมาให้ เช่น Blueprint ซึ่งอาจต้องติดตั้งอีกทีแนะนำใช้ pip

How to run :
1.เปิด Terminal (user/webstream/app)
2.พิมพ์ python app.py

@DEPLOYMENT ( การทำ Image เพื่ออัพโหลดขึ้น Cloud )

Docker :
image name : softent1

command :
1. docker built -t softent1 .
2. docker run -d --restart=always -p 80:80 -t softent1

@Version Controll ( การอัพเดทงานขึ้น Github )

1.git init

2.git commit -m "Your comment"

Ex. git commit -m "add auth.py"

#เพิ่มเติม plugin sourch Controll(VScode)
เมื่อไฟล์ถูกเปลี่ยนแปลง จะเด้งไฟล์ขึ้นใน Change
เราสามารถเพิ่ม กดเพิ่ม stage จาก change 
เมื่อเลือก stage ที่ต้องการจนครบทุกตัว ก็จะทำการ commit ใน Terminal
Changes > staged > commit

3.git remote add origin <Link to GitHub Repo>

4.git push -u origin master

#เพิ่มเติม
โปรเจคมีทั้งหมด 6 branch (6 modules)
1.master เป็นตัวที่จะ Deploy ขึ้นระบบ
2.auth
3.main
4.payment
5.register
6.vplayer

ตอน push ขึ้น git ต้องใส่ parameter ตาม branch ที่ทำ 
Ex.
ฟังก์ชันชำระเงิน payment
git push -u origin payment

ฟังก์ชันสมัครสมาชิก register
git push -u origin register

