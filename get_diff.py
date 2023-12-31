import difflib


def get_text_diff(file1,file2):
    f1 = open(file1,'r')
    f2 = open(file2,'r')
    f1text = f1.read()
    f2text = f2.read()
    # 使用difflib库生成Diff
    d = difflib.Differ()
    diff = list(d.compare(f1text.splitlines(), f2text.splitlines()))    
    return diff

def get_text_add(ori_file,modified_file):
    diff_list = get_text_diff(ori_file,modified_file)
    output = []
    for line in diff_list:
        if line.startswith('+ '):
            output.append(line[2:])
    return output



## print(get_text_add('text1','text2'))