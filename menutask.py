import os
import getpass

pas = "redhat"
pas1 = getpass.getpass()

if pas1 != pas:
	print("Incorrect Password!")
	exit()

mode = input("\n\t\t\tDo you want to run it local or remote\n").lower()
	
while True:
	os.system("clear")

	if mode == "local":
		print("\n\n\t\t\tWelcome to my tool\n")
	
		#Main-menu
		choice = int(input("\n Menu:-\n 1. Linux command\n 2. Hadoop\n 3. Docker\n 4. web-server\n 5. Find the salary\n 0. Exit\n"))	
		#Linux_command
		if choice == 1:
			l_cmd = input("\nEnter the command you want to run:-  ")
			os.system(l_cmd)
		
		#Hadoop
		elif choice == 2:
			hadoop = int(input("\n 1. Configure Hadoop\n 2. Start services\n 3. stop services\n"))
			
			#Configure Files
			if hadoop == 1:
				h_setup = int(input("\n 1. Configure as name-node\n 2. Configure as data-node\n 3. View configuration-file\n"))

				#For NAME NODE
				if h_setup == 1:
					#myfile = open('/etc/hadoop/hdfs-site.xml')
					os.chdir(r'/etc/hadoop/')
					os.system("pwd")
					f_name = input("\nEnter folder name for the data storing\n")
					c_file = "mkdir "+f_name
					os.system(c_file)
					print("\n\n\n\nWe are opening hdfs-site.xml file\n To configure as a name-node follow the steps:-\n\n 1.In <name> feild write  dfs.name.dir\n 2. In <value> feild write folder name with / ie: /{}\n 3.Press Esc\n 4. Press :\n 5. Press wq and then press enter\n".format(f_name))

					input("\nPress any key to continue")
					os.system("vim hdfs-site.xml")

					print("\n\n\n\n\n\n\t\t\t\t Now we have to configure the core-site.xml file\n")
					input("Press Enter")
					print("\n Your IP is:- \n")					
					os.system("ifconfig enp0s3")
					print("\n\n\n Steps To FOllow:- \n 1. In <value> feild after hdfs:// write your IP\n 2. Press Esc\n 3. Press :\n 4.Press wq and then press enter\n")
					
					input("\n\t\t\t\t Press any key to continue")
					os.chdir(r'/etc/hadoop/')
					os.system("pwd")
					os.system("vim core-site.xml")
					print("\n\n\n\n\n\n\n\t\t\t\tNow our files are configured\n Formating folder for use\n")
					#os.system("hadoop namenode -format")
					print("DONE..\n\nNow This device is redy to run...\n")
				

				#For DATA NODE
				elif h_setup == 2:
					os.chdir(r'/etc/hadoop/')
					os.system("pwd")
					f_name = input("\nEnter folder name for the data storing\n")
					c_file = "mkdir "+f_name
					os.system(c_file)
					print("\n\n\n\nWe are opening hdfs-site.xml file\n To configure as a name-node follow the steps:-\n\n 1.In <name> feild write  dfs.name.dir\n 2. In <value> feild write folder name with / ie: /{}\n 3.Press Esc\n 4. Press :\n 5. Press wq and then press enter\n".format(f_name))

					input("\nPress any key to continue")
					os.system("vim hdfs-site.xml")

					print("\n\n\n\n\n\n\t\t\t\t Now we have to configure the core-site.xml file\n")
					input("Press Enter")
					print("\n\n\n Steps To FOllow:- \n 1. In <value> feild after hdfs:// write IP of master node \n 2. Press Esc\n 3. Press :\n 4.Press wq and then press enter\n")
					input("\n\t\t\t\t Press any key to continue")
					os.chdir(r'/etc/hadoop/')
					os.system("pwd")
					os.system("vim core-site.xml")
					print("\n\n\n\n\n\n\n\t\t\t\tNow our files are configured\n")
					print("DONE..\n\nNow This device is redy to run...\n")

				#Show configuration file
				elif h_setup == 3:
					which = int(input(" 1. hdfs-site.xml\n 2.core-site.xml"))
					if which == 1:
						os.chdir(r'/etc/hadoop/')
						os.system("cat hdfs-site.xml")


					elif which ==2:
						os.chdir(r'/etc/hadoop/')
						os.system("cat core-site.xml")

					else:
						print("Invalid Option\n\n")

				else:
					print("Invalid Option\n\n")


			
			#Start Services				
			elif hadoop == 2:

				device = input("This Device is setup as name node or data node").lower()
				if device == "name node":
					os.system("hadoop-daemon.sh start namenode")
					os.system("jps")
					print("\nHadoop name node is started!!\n")


				elif device == "data node":
					os.system("hadoop-daemon.sh start datanode")
					os.system("jps")
					print("\nHadoop data node is started!!\n")

				else:
					print("Invalid Option\n\n")

			#Stop Services
			elif hadoop == 3:
				
				device = input("This Device is setup as name node or data node").lower()
				if device == "name node":
					os.system("hadoop-daemon.sh stop namenode")
					os.system("jps")
					print("\nHadoop name node is started!!\n")


				elif device == "data node":
					os.system("hadoop-daemon.sh stop datanode")
					os.system("jps")
					print("\nHadoop data node is started!!\n")

				else:
					print("Invalid Option\n\n")


		#Docker
		elif choice == 3:			

			docker_cmd = int(input("\n\n 1.start docker services\n 2.Run a docker container\n 3.Delete all docker container\n 4.Running containers\n 5.download the Images\n "))
			#Start/Run Container
			if docker_cmd == 1:
				print("\nStarting Container services!!.\n")
				os.system("systemctl start docker")
				print("\nDone\nService Started!!\n")

			#Run Container
			elif docker_cmd == 2:
				choose_os_image = int(input("\n 1.Ubuntu\n 2.Centos\n"))
				if choose_os_image == 1:
					os_name = "ubuntu:20.10"
				elif choose_os_image == 2:
					os.name = "centos:latest"
				else:
					print("Invalid Option\n")

				only_for_cmd = input("\n Do you want to run a container to run a command? (y)").lower()

				if only_for_cmd == "y":
					command_for_docker = input("Enter the command:- ")
				"""elif only_for_cmd == "n":
					print("You didn't select for command\n")
				else:
					print("Invalid Option!!!")
					exit()"""


				check_container_name = input("\n Do you want to give the container a name? (y)").lower()
				if check_container_name == "y":
					container_name = input("Enter container name:- ")
				"""elif only_for_cmd == "n":
					print("You didn't select for name so name will be automatically be given to the container!\n")
				else:
					print("Invalid response!!!")
					exit()"""

							

				if only_for_cmd and check_container_name == "y":
					os.system("docker run -it --name {} {} {}".format(container_name,os_name,command_for_docker))

				elif only_for_cmd == "y":
					os.system("docker run -it {} {}".format(os_name,command_for_docker))

				elif check_container_name == "y":
					os.system("docker run -it --name {} {}".format(container_name,os_name))
				
				elif check_container_name and only_for_cmd == "n":
					os.system("docker run -it {}".format(os_name))
				
				else:
					print("Invalid Option\n")

			#To Delete docker container
			elif docker_cmd == 3:
				docker_remove = "docker rm `docker ps -a -q`"
				os.system(docker_remove)

			#To see Running containers
			elif docker_cmd == 4:
				print("All running containers:- \n")
				os.system("docker ps")
			
			#TO download the OS IMAGE
			elif docker_cmd == 5:
				osimg_name = input("Enter os name:- ")
				img = ("docker pull {}".format(osimg_name))
		




		#WEB_SERVER
		elif choice == 4:
			
			option = int(input("\n 1. Start  Web-services\n 2. Stop Web-services\n 3. create a webpage\n 4. Launch a webpage\n"))

			#Start web services
			if option == 1:
				os.system("systemctl start httpd")
				print("Apache httpd server started!!\n")
			
				
			#Stop web services
			if option == 2:
				os.system("systemctl stop httpd")
				print("Apache httpd server stopped!!\n")
			
			#Create a web-page
			if option == 3:
				webpage_name = input("\nEnter file name of your webpage:- ")
				os.chdir(r'/var/www/html')
				os.system("pwd")
				if "html" in webpage_name:
					web_file_cmd = ("touch {}".format(webpage_name))
				else:
					web_file_cmd = ("touch {}.html".format(webpage_name))
				open_web_file = ("gedit {}".format(webpage_name+".html"))
				os.system(open_web_file)

			#launch webpage on firefox
			if option == 4:
				os.system("ifconfig enp0s3")
				web_ip = input("Enter your IP:- ")
				web_file =  input("Enter file name:- ")
				address = ("{}/{}".format(web_ip, web_file))
				fire_address =("firefox {}".format(address))
				os.system(fire_address)



		#Find the salary by machine Learning 
		elif choice == 5:
			continue	
		
		#Exit
		elif choice == 0:
			print("Terminating Process\n")
			os.system("sleep 3")
			os.system("clear")
			exit()



	#Remote-Login
	elif mode == "remote":

		print("Welcome to remote Login\n")


	#If it is not remote nor local
	else:
		print("Invalid Options\n")
		exit()
	
	#for pausing the screen	
	input("\n\t\t\tPress any key to continue")
