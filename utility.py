#C:\Users\pratidan\Desktop\current_switch_work.txt
import sys

filename = str(input("Enter the filename/path of file: "))
def file_Operation(option,filename):

        try:
            file = open(filename, mode="r")
        except:
            print("File not found!!! Please provide the full path of file")
            sys.exit(1)

        total_lines = 0
        total_words = 0
        total_charaters = 0
        count = 0
        count1 = 0
        for line in file:
            total_lines += 1
            line = line.strip("\n")
            words = line.split()
            for i in words:
                if i.isdigit():
                    count += 1
                if i.isalpha():
                    count1 += 1

            total_words += len(words)
            total_charaters += len(line)

        if option.lower() == "-l":
            return f'The total lines are: {total_lines}'
        elif option == "-w":
            return f"The total worlds are: {total_words}"
        elif option == "-c":
            return f"The total charater are: {total_charaters}"
        elif option == "-n":
            numeric_number = count
            return f"The total numeric number are: {numeric_number}"
        elif option == "-a":
            return f"The total alphabets are: {count1}"
        elif option == "-h":
            s = """ Please provide the following Options with filename
            Note: The options are case sensitive
            -l: To display no. of lines present in a file
            -c: To display no. of character present in a file
            -w: To display no. of words in a file
            -n: To display only numeric numbers in input file
            -a: To display only alphabets in input file
            -h: To disply help option
            exit: To exit from Applicastion"""
            return s
        elif option == "exit":
            sys.exit(1)

        else:
            s = """Option is not valid!!,please provide the correct option
want any help please provide the -h as options"""
            return s

while True:
    option = str(input("Enter the option: "))
    a = file_Operation(option,filename)
    print(a)




