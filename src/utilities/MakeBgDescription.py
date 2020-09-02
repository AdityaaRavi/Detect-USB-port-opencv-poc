# This python code was made to make a background description file

# asking the user what name the bg description file must have
while True:
    name = input("What should be the name of your file? (please include file format): ")
    num_img = int(input("How many negative images do you have? "))
    name_scheme = input("what naming scheme are you using?\nFor example, if you named each image like \"neg-5.jpeg\", "
                        "say \"neg-\" (please include path) : ")
    img_format = input("What is the extention that your file uses? \nFor example, if you named each image like \"neg-5."
                       "jpeg\", say \"jpeg\": ")
    mode = input("Do you want to add to what you already have (if any) or replace it? reply \"add\" or \"replace\": ")

    add_prefix = int(input("Do you want to add a prefix of \"0\"s? If so, type the minimum no. of digits, else type -1 : "))

    info = "Is this correct?\nYou have " + str(num_img) + " images\nYour name scheme is \"" + name_scheme + "\"\n" + \
           "Your file format is " + img_format + "\nThe name of the background description file is " + name \
           + "\nyour mode is " + mode + "\nType \"yes\" or \"no\": "

    if input(info).lower() == "yes": break

print("All right, creating the file....")
# opening the file handler in the mode given by the user
if(mode.lower() == "add"): mode = "a"
else: mode = "w"
file_handler = open(name, mode)

# creating a buffer string to store all the text until it is written to the disk.
to_write = ""
# adding the relevant text to the buffer variable
for i in range(1, num_img + 1):
    str_version = str(i)
    if add_prefix > 0:
        while len(str_version) < add_prefix:
            str_version = "0" + str_version

    to_write += name_scheme + str_version + "." + img_format + "\n\n"

# writing to the disk
file_handler.write(to_write)

# saving all the data and closing the file handler
file_handler.close()

print("Done!")

