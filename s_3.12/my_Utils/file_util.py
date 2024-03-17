def print_file_info(file_path):
    f=None
    try:
        f=open(file_path,"r",encoding="UTF-8")
        content=f.read()
        print(content)
    except Exception as e:
        print(f"出现问题了，原因是:{e}")
    finally:
        if f:f.close()

def append_to_file(file_path,content):
    f=open(file_path,"a",encoding="UTF-8")
    f.write(content)
    f.write("\n")
    f.close()

if __name__=="__main__":
    print("ok")
    append_to_file("E:\\python\\s_3.txt","船只加偶")