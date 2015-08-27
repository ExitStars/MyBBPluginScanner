#!/usr/bin/python
#-*-coding:utf-8-*-
import httplib, sys
class bgcolors:
	warning = "\033[93m"
	endc = "\033[0m"
	green = '\033[92m'
	blue = '\033[94m'
	grey = '\033[90m'
	red = '\033[91m'

eklentiler = ['kingchat.php','profilewfc.php','awaylist.php','hmflags.php','profileskype.php','socialsites.php',
'dymy_ua.php','profilefacebook.php','AJAXChat.php','youtube.php','tipsoftheday.php','profileblogs.php',
'bank.php','SuscribeUsers.php','profilealbums.php','mystatus.php','userbarplugin.php','afsignatures.php','mytabs.php']

kingchatbilgi = ["MyBB Kingchat", "XSS ve SQL Injection", "\n\thttp://www.exploit-db.com/exploits/23249/\n\thttp://www.exploit-db.com/exploits/23105/"]
profilewfcbilgi = ["MyBB Profile Wii Friend","SQL UPDATE Injection ve XSS", "\n\thttp://www.exploit-db.com/exploits/23888"]
awaylistbilgi  = ["MyBB AwayList", "SQL Injection", "\n\thttp://www.exploit-db.com/exploits/23624/"]
hmflagsbilgi = ["MyBB HM My Country Flags", "SQL Injection", "\n\thttp://www.exploit-db.com/exploits/23624/"]
profileskypebilgi = ["MyBB Profile Skype ID", "SQL Injection ve XSS", "\n\thttp://www.exploit-db.com/exploits/23382/"]
socialsitesbilgi = ["MyBB Social Sites", "XSS", "\n\thttp://www.exploit-db.com/exploits/23382/"]
dymy_uabilgi = ["MyBB DyMy User Agent", "SQL Injection", "\n\thttp://www.exploit-db.com/exploits/23359/"]
profilefacebookbilgi = ["MyBB Facebook Profile", "XSS", "\n\thttp://www.exploit-db.com/exploits/23355"]
AJAXChatbilgi = ["MyBB AJAX Chat", "XSS", "\n\thttp://www.exploit-db.com/exploits/23354/"]
youtubebilgi = ["MyBB MyYoutube", "Post SQL Injection", "\n\thttp://www.exploit-db.com/exploits/23353/"]
tipsofthedaybilgi = ["MyBB TipsOfTheDay", "-", "\n\thttp://www.exploit-db.com/exploits/23322/"]
profileblogsbilgi = ["MyBB Profile Blogs","SQL Injection ve XSS Stored", "\n\thttp://www.exploit-db.com/exploits/23287/"]
bankbilgi = ["MyBB Bank-v3", "Post SQL Injection", "\n\thttp://www.exploit-db.com/exploits/23284/"]
SuscribeUserbilgi = ["MyBB Follower User", "SQL Injection", "\n\thttp://www.exploit-db.com/exploits/22405/"]
profilealbumsbilgi = ["MyBB Profile Albums", "SQL Injection", "\n\thttp://www.exploit-db.com/exploits/22003/"]
mystatusbilgi = ["MyBB MyStatus", "SQL Injection", "\n\thttp://www.exploit-db.com/exploits/17972/"]
userbarbilgi = ["MyBB Forum Userbar", "SQL Injection", "\n\thttp://www.exploit-db.com/exploits/17962/"]
afsignaturesbilgi = ["MyBB Advanced Forum Signatures", "SQL Injection", "\n\thttp://www.exploit-db.com/exploits/17962/"]
mytabs = ["MyBB MyTabs", "SQL Injection", "\n\thttp://www.exploit-db.com/exploits/17595/"]

def logo():
	print "Code By "+bgcolors.blue+"ExitStars"+bgcolors.endc
	print "MyBB Eklenti Tarayıcı"
	print bgcolors.green+"www.Cyber-Warrior.Org"+bgcolors.endc
logo()

print "-"*60
print bgcolors.red+"Örnek:"+bgcolors.endc+" http://siteismi.com/forum"
print "-"*60
site = raw_input(bgcolors.warning+"Lütfen MyBB Siteyi Giriniz: "+bgcolors.endc)
print (bgcolors.warning+"[*] Site Test Ediliyor < "+bgcolors.endc+"{}"+bgcolors.warning+">"+bgcolors.endc).format(site)
print "-"*60

def durum_test(site, eklenti_yol):
    baglanti = httplib.HTTPConnection(site)
    baglanti.request("HEAD", eklenti_yol)
    return baglanti.getresponse().status
 

def eklenti_test(site, eklenti):
	durum = durum_test(site, "/inc/plugins/"+eklenti)
	if durum == 200:
		if eklenti == "AJAXChat.php":
			print "Açık Bulunan Eklenti: "+AJAXChatbilgi[0]+" Eklentisi"
			print "Açık Türü: Olası "+AJAXChatbilgi[1]+" Açığı"
			print "Detaylı Bilgi:"+AJAXChatbilgi[2]
			print "-"*60
		elif eklenti == "kingchat.php":
			print "Açık Bulunan Eklenti: "+kingchatbilgi[0]+" Eklentisi"
			print "Açık Türü: Olası "+kingchatbilgi[1]+" Açığı"
			print "Detaylı Bilgi:"+kingchatbilgi[2]
			print "-"*60
		elif eklenti == "profilewfc.php":
			print "Açık Bulunan Eklenti: "+profilewfcbilgi[0]+" Eklentisi"
			print "Açık Türü: Olası "+profilewfcbilgi[1]+" Açığı"
			print "Detaylı Bilgi:"+profilewfcbilgi[2]
			print "-"*60
		elif eklenti == "awaylist.php":
			print "Açık Bulunan Eklenti: "+awaylistbilgi[0]+" Eklentisi"
			print "Açık Türü: Olası "+awaylistbilgi[1]+" Açığı"
			print "Detaylı Bilgi:"+awaylistbilgi[2]
			print "-"*60
		elif eklenti == "hmflags.php":
			print "Açık Bulunan Eklenti: "+hmflagsbilgi[0]+" Eklentisi"
			print "Açık Türü: Olası "+hmflagsbilgi[1]+" Açığı"
			print "Detaylı Bilgi:"+hmflagsbilgi[2]
			print "-"*60
		elif eklenti == "profileskype.php":
			print "Açık Bulunan Eklenti: "+profileskypebilgi[0]+" Eklentisi"
			print "Açık Türü: Olası "+profileskypebilgi[1]+" Açığı"
			print "Detaylı Bilgi:"+profileskypebilgi[2]
			print "-"*60
		elif eklenti == "socialsites.php":
			print "Açık Bulunan Eklenti: "+socialsitesbilgi[0]+" Eklentisi"
			print "Açık Türü: Olası "+socialsitesbilgi[1]+" Açığı"
			print "Detaylı Bilgi:"+socialsitesbilgi[2]
			print "-"*60
		elif eklenti == "dymy_ua.php":
			print "Açık Bulunan Eklenti: "+dymy_uabilgi[0]+" Eklentisi"
			print "Açık Türü: Olası "+dymy_uabilgi[1]+" Açığı"
			print "Detaylı Bilgi:"+dymy_uabilgi[2]
			print "-"*60
		elif eklenti == "profilefacebook.php":
			print "Açık Bulunan Eklenti: "+profilefacebookbilgi[0]+" Eklentisi"
			print "Açık Türü: Olası "+profilefacebookbilgi[1]+" Açığı"
			print "Detaylı Bilgi:"+profilefacebookbilgi[2]
			print "-"*60
		elif eklenti == "youtube.php":
			print "Açık Bulunan Eklenti: "+youtubebilgi[0]+" Eklentisi"
			print "Açık Türü: Olası "+youtubebilgi[1]+" Açığı"
			print "Detaylı Bilgi:"+youtubebilgi[2]
			print "-"*60
		elif eklenti == "tipsoftheday.php":
			print "Açık Bulunan Eklenti: "+tipsofthedaybilgi[0]+" Eklentisi"
			print "Açık Türü: Olası "+tipsofthedaybilgi[1]+" Açığı"
			print "Detaylı Bilgi:"+tipsofthedaybilgi[2]
			print "-"*60
		elif eklenti == "profileblogs.php":
			print "Açık Bulunan Eklenti: "+profileblogsbilgi[0]+" Eklentisi"
			print "Açık Türü: Olası "+profileblogsbilgi[1]+" Açığı"
			print "Detaylı Bilgi:"+profileblogsbilgi[2]
			print "-"*60
		elif eklenti == "bank.php":
			print "Açık Bulunan Eklenti: "+bankbilgi[0]+" Eklentisi"
			print "Açık Türü: Olası "+bankbilgi[1]+" Açığı"
			print "Detaylı Bilgi:"+bankbilgi[2]
			print "-"*60
		elif eklenti == "SuscribeUsers.php":
			print "Açık Bulunan Eklenti: "+SuscribeUsersbilgi[0]+" Eklentisi"
			print "Açık Türü: Olası "+SuscribeUsersbilgi[1]+" Açığı"
			print "Detaylı Bilgi:"+SuscribeUsersbilgi[2]
			print "-"*60
		elif eklenti == "profilealbums.php":
			print "Açık Bulunan Eklenti: "+profilealbumsbilgi[0]+" Eklentisi"
			print "Açık Türü: Olası "+profilealbumsbilgi[1]+" Açığı"
			print "Detaylı Bilgi:"+profilealbumsbilgi[2]
			print "-"*60
		elif eklenti == "mystatus.php":
			print "Açık Bulunan Eklenti: "+mystatusbilgi[0]+" Eklentisi"
			print "Açık Türü: Olası "+mystatusbilgi[1]+" Açığı"
			print "Detaylı Bilgi:"+Amystatusbilgi[2]
			print "-"*60
		elif eklenti == "userbarplugin.php":
			print "Açık Bulunan Eklenti: "+userbarbilgi[0]+" Eklentisi"
			print "Açık Türü: Olası "+userbarbilgi[1]+" Açığı"
			print "Detaylı Bilgi:"+userbarbilgi[2]
			print "-"*60
		elif eklenti == "afsignatures.php":
			print "Açık Bulunan Eklenti: "+afsignaturesbilgi[0]+" Eklentisi"
			print "Açık Türü: Olası "+Aafsignaturesbilgi[1]+" Açığı"
			print "Detaylı Bilgi:"+afsignaturesbilgi[2]
			print "-"*60
		elif eklenti == "mytabs.php":
			print "Açık Bulunan Eklenti: "+mytabsbilgi[0]+" Eklentisi"
			print "Açık Türü: Olası "+mytabsbilgi[1]+" Açığı"
			print "Detaylı Bilgi:"+mytabsbilgi[2]
			print "-"*60
		else:
			pass		
	else:
		pass

for eklenti in eklentiler:
	eklenti_test(site, eklenti)

print "Tarama Tamamlandı, Çıkmak İçin Bir Tuşa Basınız..."
raw_input()
