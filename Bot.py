from requests import get
from re import findall
from rubika.client import Bot
import time

bot = Bot("oveddsoqdzrczpmmifddjtkhuxxuezoe")
target = "g0B2DBn0ad87ed546cf895a0aacb9812"
answered = [bot.getGroupAdmins]
retries = {}
sleeped = False
# delmess = ["دولی","کصکش","کون","کص","کیر" ,"خر","کستی","دول","گو","کس","کسکش","کوبص"]
plus= True

while True:
	try:
		admins = [i["member_guid"] for i in bot.getGroupAdmins(target)["data"]["in_chat_members"]]
		min_id = bot.getGroupInfo(target)["data"]["chat"]["last_message_id"]
		while True:
			try:
				messages = bot.getMessages(target,min_id)
				break
			except:
				continue
		
		open("id.db","w").write(str(messages[-1].get("message_id")))

		for msg in messages:
			if msg["type"]=="Text" and not msg.get("message_id") in answered:
				if not sleeped:
					if msg.get("text") == "!فعال" and msg.get("author_object_guid") in admins :
						bot.sendMessage(target, "ربات با موفقیت فعال شد✓", message_id=msg.get("message_id"))

					elif msg.get("text").startswith("!اد") :
						bot.invite(target, [bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["object_guid"]])
						bot.sendMessage(target, "کاربر با موفقیت به گپ افزوده شد✓", message_id=msg.get("message_id"))

					elif msg.get("text") == "!infobhfxFjknbvc":
						bot.sendMessage(target, "لیسـت دستـــورات ربـات 🤖:\n\n●🤖 !bot : فعال یا غیر فعال بودن بات\n\n●❎ !stop : غیر فعال سازی بات\n\n●✅ !start : فعال سازی بات\n\n●🕘 !time : ساعت\n\n●📅 !date : تاریخ\n\n●📋 !del : حذف پیام با ریپ بر روی ان\n\n●🔒 !lock : بستن چت در گروه\n\n●🔓 !unlock : باز کردن چت در گروه\n\n●❌ !ban : حذف کاربر با ریپ زدن\n\n●✉ !send : ارسال پیام با استفاده از ایدی\n\n●📌 !add : افزودن کاربر به گپ با ایدی\n\n●📜 !info : لیست دستورات ربات\n\n●🆑 !cal :ماشین حساب\n\n●🔴 !user : اطلاعات کاربر با ایدی\n\n●😂 !jok : ارسال جک\n\n●🔵 !font : ارسال فونت\n\n●🔴 !ping : گرفتن پینگ سایت\n\n●🔵 !tran : مترجم انگلیسی")
					elif msg.get("text").startswith("!حساب"):
						msd = msg.get("text")
						if plus == True:
							try:
								call = [msd.split(" ")[1], msd.split(" ")[2], msd.split(" ")[3]]
								if call[1] == "+":
									am = float(call[0]) + float(call[2])
									bot.sendMessage(target, "حاصل :\n"+"".join(str(am)), message_id=msg.get("message_id"))
									plus = False
							
								elif call[1] == "-":
									am = float(call[0]) - float(call[2])
									bot.sendMessage(target, "حاصل :\n"+"".join(str(am)), message_id=msg.get("message_id"))
							
								elif call[1] == "*":
									am = float(call[0]) * float(call[2])
									bot.sendMessage(target, "حاصل :\n"+"".join(str(am)), message_id=msg.get("message_id"))
							
								elif call[1] == "/":
									am = float(call[0]) / float(call[2])
									bot.sendMessage(target, "حاصل :\n"+"".join(str(am)), message_id=msg.get("message_id"))
							except IndexError:
								bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید ❌" ,message_id=msg.get("message_id"))
						plus= True
					elif msg.get("text").startswith("!send") :
						bot.sendMessage(bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["object_guid"], "شما یک پیام ناشناس دارید:\n"+" ".join(msg.get("text").split(" ")[2:]))
						bot.sendMessage(target, "پیام با موفقیت ارسال شد✓", message_id=msg.get("message_id"))
						#دیگو گرام
					elif msg.get("text") == "سلام":
						bot.sendMessage(target, "سلام عزیز من گل من عخش من", message_id=msg.get("message_id"))
						
						bot.sendMessage(target, "سلام عشقم چطوری ؟ ❤😍", message_id=msg.get("message_id"))

					elif msg.get("text") == "بیا بخورش" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "کونتو؟", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "اره" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "😐مبارکه", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "نه" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "اهمیت ندادم", message_id=msg.get("message_id"))

					elif msg.get("text") == "خوبی" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "ممنون به خوبیت تو خوبی؟", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "سلامتی" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "همیشه سلامت باشی گلم♥️", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "ایول" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "بنازم به ایول گفتنت😍", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "😡" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "چیز اضافی خودم😐💔", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "چقدر منو دوست داری" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "خیلی دوست دارم انقد که گفتنی نیست😊❤️", message_id=msg.get("message_id"))
						#دیکو گرام
					elif msg.get("text") == "استقلال" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "قسم به تیم استقلال ، قسم به سیمای خوبان ، قسم به ناصر حجازی ، ندای ما استقلال 💙", message_id=msg.get("message_id"))
						#دیگو گرام
					elif msg.get("text") == "💙" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "قسم به تیم استقلال ، قسم به سیمای خوبان ، قسم به ناصر حجازی ، ندای ما استقلال 💙", message_id=msg.get("message_id"))
						#دیگو گرام
					elif msg.get("text") == "پرسپولیس" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "پرسپولیس عشق آسیایی پرسپولیس خالق یک جامی گل بزن امشبو به یاد پروین و علی دایی ❤", message_id=msg.get("message_id"))
						#دیگو گرام
					elif msg.get("text") == "❤" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "پرسپولیس عشق آسیایی پرسپولیس خالق یک جامی گل بزن امشبو به یاد پروین و علی دایی ❤", message_id=msg.get("message_id"))
						#دیگو گرام
					elif msg.get("text") == "😎" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "هر کی با ما در افتاد ور افتاد 😎", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "😂" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "خنده خنده می اورد", message_id=msg.get("message_id"))
						#دیگو گرام
					elif msg.get("text") == "😐" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "بخورش", message_id=msg.get("message_id"))
						#دیگو گرام
					elif msg.get("text") == "😂😂" and msg.get("author_object_guid") :
						#دیگو گرام
						bot.sendMessage(target, "حون باوا", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "ممد" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "بمال فری هر روز براش ساک میزنه [فریم برای‌حسین‌میزنه (ساک)]", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "حسین" and msg.get("author_object_guid") :
						#دیگو گرام
						bot.sendMessage(target, "ریس منه عشق منه(حسین تیاماروس)", message_id=msg.get("message_id"))
						#دیگو گرام
					elif msg.get("text") == "چی بلدی" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "بطچ؟", message_id=msg.get("message_id"))
						#دیگو گرام
					elif msg.get("text") == "لینک" and msg.get("author_object_guid") :
						
						bot.sendMessage(target,"https://rubika.ir/joing/BCCCHIDE0FVLGWOPXCEEQYPQFUHYHIAB", message_id=msg.get("message_id"))
						#دیگو گرام
					elif msg.get("text") == "گوه نخور" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "شب میرینم صبح بخور", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "ربات" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "ها", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "خودتو معرفی کن" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "من ربات هستم که با هوش مصنوعی میتونم اینجا رو مدیریت کنم و باهاتون مثل یک انسان واقعی چت کنم", message_id=msg.get("message_id"))
						#دیگو گرام
					elif msg.get("text") == "ممنون" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "خواهش میکنم گلم💋😌", message_id=msg.get("message_id"))
						#دیگو کرام
					elif msg.get("text") == "بای" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "کجا میری بودی حالا 😕", message_id=msg.get("message_id"))
						#دیگو گرام
					elif msg.get("text") == "چه خبر" and msg.get("author_object_guid") :
						#دیگو گرام
						bot.sendMessage(target, "سلامتی خوبم میگذرونم دیگه", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "عشق" and msg.get("author_object_guid") :
						#دیگو گرام
						bot.sendMessage(target, "😊❤️", message_id=msg.get("message_id"))
						#دیگو گرام
					elif msg.get("text") == "منم خوبم" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "خدا رو شکر 😘", message_id=msg.get("message_id"))
#دیگو گرام
					elif msg.get("text") == "فدات" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "خدا نکنه قربونت 😁❤️", message_id=msg.get("message_id"))
						#دیگو کرام
					elif msg.get("text") == "بی تر ادب" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "اره دا تو همینم نیستی 😏", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "هعی" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "زر نزن باو", message_id=msg.get("message_id"))
						#دیگو کرام
					elif msg.get("text") == "مرسی" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "🥰", message_id=msg.get("message_id"))
						#دیگو گرام
					elif msg.get("text") == "فری" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "زیر خواب حسین تیاماروس هر روز براش ساک میزنه", message_id=msg.get("message_id"))

					if  msg.get("text").startswith('!user @'):
						try:
							user_info = bot.getInfoByUsername( msg.get("text")[7:])
							if user_info['data']['exist'] == True:
								if user_info['data']['type'] == 'User':
									bot.sendMessage(target, 'Name User:\n ' + user_info['data']['user']['first_name'] + ' ' + user_info['data']['user']['last_name'] + '\n\nBio User:\n ' + user_info['data']['user']['bio'] + '\n\nGuid:\n ' + user_info['data']['user']['user_guid'] ,  msg.get('message_id'))
									print('sended response')
								else:
									bot.sendMessage(target, 'کانال است ❌' ,  msg.get('message_id'))
									print('sended response')
							else:
								bot.sendMessage(target, "کاربری وجود ندارد ❌" ,  msg.get('message_id'))
								print('sended response')
						except:
							print('server bug6')
							bot.sendMessage(target, "خطا در اجرای دستور مجددا سعی کنید ❌" ,message_id=msg.get("message_id"))
							

					elif msg.get("text") == "!خاموش" and msg.get("author_object_guid") in admins :
						sleeped = True
						bot.sendMessage(target, "ربات با موفقیت غیرفعال شد✓", message_id=msg.get("message_id"))

					elif msg.get("text").startswith("!پینگ"):
						
						try:
							responser = get(f"https://api.codebazan.ir/ping/?url={msg.get('text').split()[1]}").text
							bot.sendMessage(target, responser,message_id=msg["message_id"])
						except:
							bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید ❌", message_id=msg["message_id"])

					elif msg.get("text").startswith("!ترجمه"):
						
						try:
							responser = get(f"https://api.codebazan.ir/translate/?type=json&from=en&to=fa&text={msg.get('text').split()[1:]}").json()
							al = [responser["result"]]
							bot.sendMessage(msg.get("author_object_guid"), "پاسخ به ترجمه:\n"+"".join(al)).text
							bot.sendMessage(target, "نتیجه به پیوی شما ارسال شد ✅", message_id=msg["message_id"])
						except:
							bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید ❌", message_id=msg["message_id"])

					elif msg.get("text").startswith("!فونت"):
						#print("\n".join(list(response["result"].values())))
						try:
							response = get(f"https://api.codebazan.ir/font/?text={msg.get('text').split()[1]}").json()
							bot.sendMessage(msg.get("author_object_guid"), "\n".join(list(response["result"].values())[:110])).text
							bot.sendMessage(target, "نتیجه به پیوی شما ارسال شد ✅", message_id=msg["message_id"])
						except:
							bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید ❌", message_id=msg["message_id"])



					elif msg.get("text").startswith("!جوک"):
						
						try:
							response = get("https://api.codebazan.ir/jok/").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید ❌", message_id=msg["message_id"])

					elif msg.get("text") == "!ساعت":
						bot.sendMessage(target, f"Time : {time.localtime().tm_hour} : {time.localtime().tm_min} : {time.localtime().tm_sec}", message_id=msg.get("message_id"))

					elif msg.get("text") == "!dhdhdhdhhate":
						bot.sendMessage(target, f"Date: {time.localtime().tm_year} / {time.localtime().tm_mon} / {time.localtime().tm_mday}", message_id=msg.get("message_id"))

					elif msg.get("text") == "!پاک" and msg.get("author_object_guid") in admins :
						bot.deleteMessages(target, [msg.get("reply_to_message_id")])
						bot.sendMessage(target, "پیام پاک شد ✓", message_id=msg.get("message_id"))

					# elif msg.get("text").split(" ")[0] in  delmess:
					# 	bot.deleteMessages(target, [msg.get("message_id")])
					# 	bot.sendMessage(target, "یک پیام مستهجن پاک شد ✅", message_id=msg.get("message_id"))


					elif msg.get("text") == "!قفل" and msg.get("author_object_guid") in admins :
						print(bot.setMembersAccess(target, ["ViewMembers","ViewAdmins","AddMember"]).text)
						bot.sendMessage(target, "گپ بسته شد✓", message_id=msg.get("message_id"))

					elif msg.get("text") == "!باز" and msg.get("author_object_guid") in admins :
						bot.setMembersAccess(target, ["ViewMembers","ViewAdmins","SendMessages","AddMember"])
						bot.sendMessage(target, "گپ باز شد ✓", message_id=msg.get("message_id"))

					elif msg.get("text").startswith("!بن") and msg.get("author_object_guid") in admins :
						try:
							guid = bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["abs_object"]["object_guid"]
							user = bot.getUserInfo(data['peer_objects'][0]['object_guid'])["data"]["user"]["first_name"]
							if not guid in admins :
								bot.banGroupMember(target, guid)
								bot.sendMessage(target, f"کاربر با موفقیت حذف شد.✓", message_id=msg.get("message_id"))
							else :
								bot.sendMessage(target, f"خطایی رخ داده است×", message_id=msg.get("message_id"))
								
						except IndexError:
							a = bot.getMessagesInfo(target, [msg.get("reply_to_message_id")])[0]["author_object_guid"]
							if a in admins:
								bot.sendMessage(target, f"کاربر حذف نشد×", message_id=msg.get("message_id"))
							else:
								bot.banGroupMember(target, bot.getMessagesInfo(target, [msg.get("reply_to_message_id")])[0]["author_object_guid"])
								bot.sendMessage(target, f"کاربر حذف شد ✓", message_id=msg.get("message_id"))

				else:
					if msg.get("text") == "!روشن" and msg.get("author_object_guid") in admins :
						sleeped = False
						bot.sendMessage(target, "ربات با موفقیت فعال شد✓", message_id=msg.get("message_id"))

			elif msg["type"]=="Event" and not msg.get("message_id") in answered and not sleeped:
				name = bot.getGroupInfo(target)["data"]["group"]["group_title"]
				data = msg['event_data']
				if data["type"]=="RemoveGroupMembers":
					user = bot.getUserInfo(data['peer_objects'][0]['object_guid'])["data"]["user"]["first_name"]
					bot.sendMessage(target, f"کاربر به دلیل رعایت نکردن قوانین از گروه حذف و محروم شد.✓", message_id=msg["message_id"])
				
				elif data["type"]=="AddedGroupMembers":
					user = bot.getUserInfo(data['peer_objects'][0]['object_guid'])["data"]["user"]["first_name"]
					bot.sendMessage(target, f"سلام کاربر {user} به گروه {name} خوش اومدید 😃\nلطفا قوانین رو رعایت کن ✅", message_id=msg["message_id"])
				
				elif data["type"]=="LeaveGroup":
					user = bot.getUserInfo(data['performer_object']['object_guid'])["data"]["user"]["first_name"]
					bot.sendMessage(target, f"یک پیام دارم برای تویی که لفت دادی😐...", message_id=msg["message_id"])
					
				elif data["type"]=="JoinedGroupByLink":
					user = bot.getUserInfo(data['performer_object']['object_guid'])["data"]["user"]["first_name"]
					bot.sendMessage(target, f"سلام کاربر {user}  به گروه {name} خوش اومدید 😃\nلطفا قوانین رو رعایت کن ✅", message_id=msg["message_id"])

			answered.append(msg.get("message_id"))

	except KeyboardInterrupt:
		exit()

	except Exception as e:
		if type(e) in list(retries.keys()):
			if retries[type(e)] < 3:
				retries[type(e)] += 1
				continue
			else:
				retries.pop(type(e))
		else:
			retries[type(e)] = 1
			continue


