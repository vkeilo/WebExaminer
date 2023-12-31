from fwatch import dir_scanner
from dir_back import backup_folder
from agent_use import  gpt_agent 
from get_diff import get_text_add
import shutil
import time
import os





def get_back_file(ori_file, target_dir, backup_dir):
    traget_file_abs = os.path.abspath(target_dir)
    backup_dir_abs = os.path.abspath(backup_dir)
    # 获取原始文件的相对路径
    rel_path = os.path.relpath(ori_file, traget_file_abs)
    # 构建备份文件的绝对路径
    backup_file_abs = os.path.join(backup_dir_abs, rel_path)
    return backup_file_abs

# print(get_back_file('/media/vkeilo/Titan/git_workspace/Api_use/gpt-api-use/API测试.ipynb', target_dir, backup_dir))
def examine_file(check_file,back_file):
    added_text_list = get_text_add(back_file,check_file)
    shutil.copy(check_file, back_file)
    if(len(added_text_list) == 0):
        return
    print(added_text_list)
    gpt_assis.prompt_add("新增的内容：\n"+str(added_text_list))
    print(gpt_assis.prompt_post(T=0.6,remember_flag=True))
    # gpt_assis.init_role()











if __name__ == "__main__":
    target_dir = 'test'
    backup_dir = 'tmpdir'
    backup_folder(target_dir, backup_dir)

    gpt_assis = gpt_agent('chatglm2-6b')
    gpt_assis.init_messages_by_json('examiner.json')
    test_scanner = dir_scanner(target_dir)
    test_scanner.start_log()
    gpt_assis.start_interact()



    while True:
        if len(test_scanner.needcheck_list) > 0:
            check_file = test_scanner.needcheck_list[0]
            print(f'检测含新内容的文件\t{check_file}')
            test_scanner.need_check_remove(check_file)
            back_file = get_back_file(check_file,target_dir,backup_dir)
            examine_file(check_file,back_file)
        else:
            time.sleep(0.3)



