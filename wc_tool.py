import argparse
import os

def count_lines_words_characters_bytes(filename):
    with open(filename,'r',encoding='utf-8') as file:
        lines_list = file.readlines()
        lines = len(lines_list)
        words = sum(len(line.split()) for line in lines_list)
        characters = sum((len(line)+1) for line in lines_list) 

    bytes = os.stat(filename).st_size

    return (lines,words,characters,bytes)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(prog="WC Tool",description="Unix version of WC tool")
    parser.add_argument("filename")
    parser.add_argument('-c','--bytes',action='store_true',help="print the byte counts")
    parser.add_argument('-m','--chars',action='store_true',help="print the character counts")
    parser.add_argument('-w','--words',action='store_true',help="print the word counts")
    parser.add_argument('-l','--lines',action='store_true',help="print the newline counts")
    args = parser.parse_args()

    filename = f"{args.filename}"
    try:
        lines,words,characters,bytes = count_lines_words_characters_bytes(filename)

        output_str = ""
        if (args.lines): 
            output_str += f"{lines} "

        if (args.words):
            output_str += f"{words} "

        if (args.chars):
            output_str += f"{characters} "

        if (args.bytes):
            output_str += f"{bytes} "
        
        if (len(output_str) == 0):
            output_str += f"{lines} {words} {bytes} "
        
        output_str += filename
        print(output_str)
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except Exception as e:
        print(f"An error occured: {e}")

