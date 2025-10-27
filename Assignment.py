import pyfiglet

name=input("Enter Your Name: ")
reg_no=input("Enter Your Reg Number: ")

name_banner=pyfiglet.figlet_format(name, font="ansi_shadow")
reg_no_banner=pyfiglet.figlet_format(reg_no, font="ansi_shadow")

print(name_banner)
print(reg_no_banner)
