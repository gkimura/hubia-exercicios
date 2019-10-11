import reverse
import grep

file_name = input("Insira nome do arquivo: ")
"""
reverse.reverse_file(file_name)
reverse.reverse_lines(file_name)
"""
string = input("Insira string para buscar no arquivo: ")
grep.grep(string,file_name)
