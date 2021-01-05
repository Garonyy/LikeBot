import amino
import os
client=amino.Client()
er=False
while er==False:
	try:
		os.system("clear")
		print("\033[1;36m Amino :  \033[1;34mSirLez \n \n \033[1;36minsta : \033[1;34m SirLe0x \n \n \n")
		e=input("\033[1;32m# \033[1;33memail \033[1;32m:\033[1;0m ")
		p=input("\033[1;32m# \033[1;33mpasswrod \033[1;32m:\033[1;0m ")
		client.login(email=e,password=p)
		er=True
	except:
			er=False
			i=input("\n\033[1;32m# \033[1;31maccount is valid!\n\n\033[1;32m# \033[1;33mdo u want to continue? \033[1;32my\033[1;33m/\033[1;32mn \033[1;33m: \033[1;0m")
			if i =='n' or i =='N' or i =='no' or i =='No':
				os._exit(1)
				
				
infoos=input("\033[1;32m# \033[1;33mcommunity url\033[1;32m : \033[0m")
infoo=client.get_from_code(infoos)
comId=infoo.path[1:infoo.path.index("/")]
sub_client=amino.SubClient(comId=comId,profile=client.profile)

s=int(input("\033[1;32m#\033[1;33m how many blogs?\033[1;32m : \033[0m"))
os.system("clear")
nm=0
while s > nm and len:
	lb=sub_client.get_recent_blogs(start=nm,size=s).blogId
	b=0
	for id in lb:
		try:
			sub_client.like_blog(blogId=id)
			print("\033[1;92m",b,"- \033[1;93mblog id \033[1;92m=\033[1;93m",id)
			b=b+1
		except:
				f=True
				nm=nm+25


print("\033[1;92mall finished !\033[0m")

os._exit(1)
