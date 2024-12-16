import argparse
import os
import sys

def count_lines_words_characters_bytes(file_content):
    lines_list = file_content.splitlines()
    lines = len(lines_list)
    words = sum(len(line.split()) for line in lines_list)
    characters = sum((len(line)+1) for line in lines_list) 
    bytes = len(file_content.encode('utf-8'))


    return (lines,words,characters,bytes)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(prog="WC Tool",description="Unix version of WC tool")
    parser.add_argument("filename",
                        type=str,
                        nargs='?',
                        help="Path to the file to process. Reads from stdin if not provided.")
    
    parser.add_argument('-c','--bytes',action='store_true',help="print the byte counts")
    parser.add_argument('-m','--chars',action='store_true',help="print the character counts")
    parser.add_argument('-w','--words',action='store_true',help="print the word counts")
    parser.add_argument('-l','--lines',action='store_true',help="print the newline counts")
    args = parser.parse_args()

    filename = f"{args.filename}"
    try:
        if (args.filename):
            with open(args.file, 'r', encoding='utf-8') as file_handle:
                content = file_handle.read()


        else:
            print("Reading from standard input. Press Ctrl+D (Unix) or Ctrl+Z (Windows) to finish.")
            content = sys.stdin.read()

        lines,words,characters,bytes = count_lines_words_characters_bytes(content)
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
        
        if (args.filename):
            output_str += filename
        else:
            output_str += "stdin"
        print(output_str)

    except FileNotFoundError:
        print(f"File {filename} not found.")
    except Exception as e:
        print(f"An error occured: {e}")

