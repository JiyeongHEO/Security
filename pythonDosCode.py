
#1. os.system("cmd")을 사용하십시오

#2. Popen 모듈을 사용하여 새로운 process를 생성하십시오.

#3.프로세스의 반환 값을 얻으십시오. 프로세스가 종료되지 않은 경우 None.을 반환합니다.

p= Popen("cp -rf a/* b/", shell=True, stdout=PIPE, stderr=PIPE)
p.wait()
if p.returncode != 0:
    print "Error"
    return -1
  
#3. commands.getstatusoutput 메소드를 사용하십시오
status,output = commands.gettatusoutput("ls")

