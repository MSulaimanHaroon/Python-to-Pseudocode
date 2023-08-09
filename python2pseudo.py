import re

python_file = 'file.py'
basic_conversion_rules = {"for": "FOR", "=": "TO", "if": "IF", "==": "EQUALS", "while": "WHILE", "until": "UNTIL", "import": "IMPORT", "class": "DEFINE CLASS", "def": "DEFINE FUNCTION", "else:": "ELSE:", "elif": "ELSEIF", "except:": "EXCEPT:", "try:": "TRY:", "pass": "PASS", "in": "IN"}
prefix_conversion_rules = {"=": "SET ", "#F": "CALL "}
advanced_conversion_rules = {"print": "OUTPUT", "return": "RETURN", "input": "INPUT"}

def f2list(to_list):
    return to_list.readlines()

def l2pseudo(to_pseudo):
    new_pseudo = []
    for line in to_pseudo:
        line = re.split(r'(\s+)', line)
        for idx, word in enumerate(line):
            if word in prefix_conversion_rules:
                if idx == 0 and line[idx]:  
                    line[idx] = prefix_conversion_rules[word] + line[idx]
                elif idx > 1: 
                    line[idx] = prefix_conversion_rules[word] + line[idx]
            elif word in basic_conversion_rules:
                line[idx] = basic_conversion_rules[word]
            elif word in advanced_conversion_rules:
                line[idx] = advanced_conversion_rules[word]
        new_pseudo.append("".join(line))
    return new_pseudo

def p2file(to_file):
    with open(python_file + '_pseudo.txt', 'w') as file:
        for line in to_file:
            print(line, file=file)

def main():
    with open(python_file, 'r+') as main_file:
        work_file = f2list(main_file)
        work_file = l2pseudo(work_file)
        p2file(work_file)
        print("Conversion complete.")
    

if __name__ == "__main__":
    main()
    
