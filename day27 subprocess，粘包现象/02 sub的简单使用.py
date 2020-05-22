import subprocess

cmd = input("请输入你要执行的指令：")
sub_obj = subprocess.Popen(
    cmd,  # 要执行的系统指令
    shell = True ,  # 固定
    stdout = subprocess.PIPE,  # 标准信息输出对象，管道，保存着指令的执行结果
    stderr = subprocess.PIPE   # 标准错误信息输出
)

print('正确输出',sub_obj.stdout.read().decode('gbk'))
print('错误输出',sub_obj.stderr.read().decode('gbk'))