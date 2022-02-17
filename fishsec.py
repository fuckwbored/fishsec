import os
import colorama
import pyshorteners as sh
import pyshorteners
from colorama import init
from colorama import Fore, Back, Style

init(autoreset=True)
s = pyshorteners.Shortener()
s = sh.Shortener()

# Укоротить ссылку
def cutlink():
	try:
		isgd = s.isgd.short(link__input)
		dagd = s.dagd.short(link__input)
		osdb = s.osdb.short(link__input)
		tinyurl = s.tinyurl.short(link__input)
		print("[" + Fore.GREEN + "ГОТОВО" + Fore.WHITE + "] Ссылки сгенерированы успешно: \n")
		print(f'{isgd} \n{dagd} \n{osdb} \n{tinyurl}')
	except:
		print("[" + Fore.RED + "ОШИБКА" + Fore.WHITE + "] Убедитесь, что ссылка корректа и повторите попытку!")

# Маскировка ссылки
def masklink():
	print("[" + Fore.GREEN + "ГОТОВО" + Fore.WHITE + "] Ссылки сгенерированы успешно: \n")
	print("https://vk.com/away.php?photo435_33&to=" + link_input)
	print("https://www.youtube.com/redirect?q=" + link_input)
	print("https://www.google.com/url?q=" + link_input)
	print("https://m.ok.ru/dk?__dp=y&_prevCmd=altGroupMain&st.cln=off&st.cmd=outLinkWarning&st.rfn=" + link_input)
	print("https://l.facebook.com/l.php?u=" + link_input)
	print("https://raidforums.com/misc.php?action=safelinks&url=" + link_input)

# Пункты и баннер

banner = Fore.RED + """

  █████▒██▓  ██████  ██░ ██   ██████ ▓█████  ▄████▄  
▓██   ▒▓██▒▒██    ▒ ▓██░ ██▒▒██    ▒ ▓█   ▀ ▒██▀ ▀█  
▒████ ░▒██▒░ ▓██▄   ▒██▀▀██░░ ▓██▄   ▒███   ▒▓█    ▄ 
░▓█▒  ░░██░  ▒   ██▒░▓█ ░██   ▒   ██▒▒▓█  ▄ ▒▓▓▄ ▄██▒
░▒█░   ░██░▒██████▒▒░▓█▒░██▓▒██████▒▒░▒████▒▒ ▓███▀ ░
 ▒ ░   ░▓  ▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ░▒ ▒  ░
 ░      ▒ ░░ ░▒  ░ ░ ▒ ░▒░ ░░ ░▒  ░ ░ ░ ░  ░  ░  ▒   
 ░ ░    ▒ ░░  ░  ░   ░  ░░ ░░  ░  ░     ░   ░        
        ░        ░   ░  ░  ░      ░     ░  ░░ ░      
                                            ░        
""" + Fore.WHITE

maintext = f"""
{banner}
[1] Маскировать ссылку (через редирект)
[2] Укоротить ссылку
"""
os.system("termux-open-url https://t.me/termuxqew")

# Основная часть
while True:
	print(maintext)
	user_input = input('>>> ')

	if user_input == "1":
		print("[?] Укажи ссылку какую нужно замаскировать с http/https. Например: \nhttps://fishing-link.com \n")
		link_input = input(">>> ")
		masklink()

	elif user_input == '2':
		print("[?] Укажи ссылку какую нужно укоротить с http/https. Например: \nhttps://fishing-link.com \n")
		link__input = input(">>> ")
		cutlink()
	else:
		print("[" + Fore.RED + "ОШИБКА" + Fore.WHITE + "] Не верный выбор! Повторите попытку")