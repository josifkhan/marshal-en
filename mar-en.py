# // developed by : Md Josif Khan
# x_x


from marshal import *
import os,sys,time
from datetime import datetime as d
from termcolor import colored

def encryptor():

	R='\033[1;31;40m'
	G='\033[1;32;40m'
	Y='\033[1;33;40m'
	B='\033[1;34;40m'
	M='\033[1;35;40m'
	C='\033[1;36;40m'
	E='\033[1;37;40m'
	E1='\033[1;0m'

	os.system('clear')
	banner=colored(f"""
	███╗   ███╗ █████╗ ██████╗       ███████╗███╗   ██╗
	████╗ ████║██╔══██╗██╔══██╗      ██╔════╝████╗  ██║
	██╔████╔██║███████║██████╔╝█████╗█████╗  ██╔██╗ ██║
	██║╚██╔╝██║██╔══██║██╔══██╗╚════╝██╔══╝  ██║╚██╗██║
	██║ ╚═╝ ██║██║  ██║██║  ██║      ███████╗██║ ╚████║
	╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝      ╚══════╝╚═╝  ╚═══╝
	____________________________________________________
	              Coded By : Md Josif Khan
	                    {G}fb/josifvai\033[1;0m
	                                                   
	""","red")

	print(banner)
	f=input(f'{R}[+]open{E}>>')

	if len(f)==0 or f=='':
		print(f"{R}[+] Failed{E1}: {Y}No input file detected!{E1}")
		time.sleep(2)
		encryptor()
		sys.exit()


	try:
		op=open(f,'r').read()
	except FileNotFoundError:
		print(f"{R}[+] Failed{E1}: {Y}No file found named '{f}', try again.{E1}")
		time.sleep(2)
		encryptor()
		sys.exit()
	except UnicodeDecodeError:
		print(f"{R}[+] Failed{E1}: {Y}Windows does not support bigger file encryption. Use Linux or Termux (Android){E1}")

	

	xt=time.strftime('%X')
	try:
		op=compile(op,'<josif>','exec')
		x=repr(dumps(op))
	except:
		print(f"{R}[+] Failed{E1}: {Y}to encryt your code!{E1}")
		sys.exit()

	enc=f"""
from marshal import *
exec(loads({x}))
"""
	open(f'en-{f}','w').write(enc)
	print(f'''
[+] {R}Started at{E} : {G}{xt}{E}
[+] {R}Filename{E} : {G}{f}{E},
[+] {R}Status{E} : {G}success, saved as '{Y}en-{f}{E1}'{E},
[+] {R}Compiled Time{E} : {G}{d.now()}{E}.
''')
	



encryptor()


