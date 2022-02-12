
import binascii
import tkinter as tk
import tkinter.filedialog
import hashlib
from blake3 import blake3
from tkinter import scrolledtext 
# import subprocess

b2sum = ""
file = ''
codes = {}
def onFinish():
    pass

def findfile():
    global file
    file = tkinter.filedialog.askopenfilename()
    if file != '':
        b2.config(text = "File in："+ file)
        start()
    else:
        b2.config(text = "Please select a file")
    
# def blake2(alg):
#     global codes
    
#     alg = "blake2"+alg
#     cwd = os.getcwd()
#     tool = os.path.abspath(cwd + '/bin/b2sum-i686-windows.exe')

#     cmd = '"'+ tool +'"'  + " "+"-a "+alg+" "+ '"'+ os.path.abspath(file) + '"'
#     if alg == "blake23":
#         alg = "blake3"
#         cmd = '"'+os.path.abspath(cwd + '/bin/b3sum_windows_x64_bin.exe')+'"'  + ' ' + '"'+ os.path.abspath(file) + '"'


#     code = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE).stdout.readlines()
#     print(cmd)

#     try:
#         if code != []:
#             code = code[0].decode("utf-8").split(" ")[0]
#     except:
#         if code != []:
#             code =  code[0].decode("gbk").split(" ")[0]
#     if code != []:
#         codes[alg] = code
#     else:
#         codes[alg] = "error" 

def calHashForBigFile(a):
    global file
    if a == "md5":
        m = hashlib.md5()
    elif a == "sha1":
        m = hashlib.sha1()
    elif a == 'sha224':
        m = hashlib.sha224()
    elif a == 'sha256':
        m = hashlib.sha256()
    elif a == 'sha384':
        m = hashlib.sha384()
    elif a == 'hmac':
        m = hashlib.sha384()
    elif a == 'blake2b':
        m = hashlib.blake2b()
    elif a == 'blake2s':
        m = hashlib.blake2s()
    elif a == 'blake3':
        m = blake3()
    f = open(file, 'rb')
    buffer = 8192    # why is 8192 | 8192 is fast than 2048
    while 1:
        chunk = f.read(buffer)
        if not chunk : break
        m.update(chunk)     
    f.close()
    return m.hexdigest()
def calcFileCRC(): 
    global file
    try: 
        blocksize = 1024 * 64 
        f = open(file,"rb") 
        str = f.read(blocksize) 
        crc = 0 
        while(len(str) != 0): 
            crc = binascii.crc32(str, crc) 
            str = f.read(blocksize) 
        f.close() 
    except: 
        print('get file crc error!') 
        return "error"
    return hex(crc)
def start():
    global codes
    codes = {}
    if blake2b.get() == 1:
        codes['blake2s'] = calHashForBigFile("blake2b")
    if blake2s.get() == 1:
        codes['blake2b'] = calHashForBigFile("blake2s")
    if blake2bp.get() == 1:
        codes['blake2bp'] = "unsuport"
    if blake2sp.get() == 1:
        # blake2("sp")
        codes['blake2sp'] = "unsuport"
    if md5.get() == 1:
        codes['md5'] = calHashForBigFile('md5')
    if blake3i.get() == 1:
        codes['blake3'] = calHashForBigFile("blake3")
    if crc32.get() == 1:
        codes['crc32'] = calcFileCRC()
    if hmac.get() == 1:
         codes['hmac'] = calHashForBigFile('hmac')
    if sha1.get() == 1:
        codes['sha1'] = calHashForBigFile('sha1')
    if sha224.get() == 1:
        codes['sha224'] = calHashForBigFile('sha224')
    if sha256.get() == 1:
        codes['sha256'] = calHashForBigFile('sha256')
    if sha384.get() == 1:
        codes['sha384'] = calHashForBigFile('sha384')
    text = ""
    for k in codes.keys():
        text = text +"[ " +k.upper()+"\t]" + "\t" + codes[k] + '\n'
    b4.delete(1.0, tk.END)
    max_height = len(codes.keys()) + 3
    maxchar = max(len(l) for l in text.split('\n'))
    max_width = max(60, min(144, maxchar - 20))
    b4.configure(width= max_width)
    b4.configure(height= max_height)
    b4.insert(tk.END,text)


if __name__ == "__main__":
    
    root = tk.Tk()
    root.title("File Checksum toolkit")
    # root.iconbitmap("icon.ico")
    b1 = tk.Label(root, text = '1.Choose system')
    b1.pack()
    sys_code = tk.IntVar()
    
    windows64_select = tk.Radiobutton(root, text='Windows amd64',value=1,variable=sys_code)
    windows86_select = tk.Radiobutton(root, text='Windows x86',value=2,variable=sys_code)
    windows64_select.pack()
    windows86_select.pack()
    b3 = tk.Label(root, text = '2.Choose Algrithom')
    b3.pack()
    frame1 = tk.Frame(root)
    frame2 = tk.Frame(root)
    frame3 = tk.Frame(root)
    blake2b = tk.IntVar()
    blake2s = tk.IntVar()
    blake2bp = tk.IntVar()
    blake2sp = tk.IntVar()
    C1 = tk.Checkbutton(frame1, text = "blake2b", variable = blake2b, onvalue = 1, offvalue = 0)
    C2 = tk.Checkbutton(frame1, text = "blake2s", variable = blake2s, onvalue = 1, offvalue = 0)
    C3 = tk.Checkbutton(frame1, text = "blake2bp", variable = blake2bp, onvalue = 1, offvalue = 0)
    C4 = tk.Checkbutton(frame1, text = "blake2sp", variable = blake2sp, onvalue = 1, offvalue = 0)

    md5 = tk.IntVar()
    blake3i = tk.IntVar()
    crc32 = tk.IntVar()
    hmac = tk.IntVar()
    C5 = tk.Checkbutton(frame2, text = "md5", variable = md5, onvalue = 1, offvalue = 0)
    C6 = tk.Checkbutton(frame2, text = "blake3", variable = blake3i, onvalue = 1, offvalue = 0)
    C7 = tk.Checkbutton(frame2, text = "crc32", variable = crc32, onvalue = 1, offvalue = 0)
    C8 = tk.Checkbutton(frame2, text = "hmac", variable = hmac, onvalue = 1, offvalue = 0)

    sha1 = tk.IntVar()
    sha224 = tk.IntVar()
    sha256 = tk.IntVar()
    sha384 = tk.IntVar()
    C9 = tk.Checkbutton(frame3, text = "sha1", variable = sha1, onvalue = 1, offvalue = 0)
    C10 = tk.Checkbutton(frame3, text = "sha224", variable = sha224, onvalue = 1, offvalue = 0)
    C11 = tk.Checkbutton(frame3, text = "sha256", variable = sha256, onvalue = 1, offvalue = 0)
    C12 = tk.Checkbutton(frame3, text = "sha384", variable = sha384, onvalue = 1, offvalue = 0)
    
    C1.pack(side=tk.LEFT)
    C2.pack(side=tk.LEFT)
    C3.pack(side=tk.LEFT)
    C4.pack(side=tk.LEFT)
    C5.pack(side=tk.LEFT)
    C6.pack(side=tk.LEFT)
    C7.pack(side=tk.LEFT)
    C8.pack(side=tk.LEFT)
    C9.pack(side=tk.LEFT)
    C10.pack(side=tk.LEFT)
    C11.pack(side=tk.LEFT)
    C12.pack(side=tk.LEFT)

    frame1.pack(side=tk.TOP)
    frame2.pack(side=tk.TOP)
    frame3.pack(side=tk.TOP)



    file_btn = tk.Button(root,text="3.Choose File And Calculate Checksum",command=findfile)
    file_btn.pack()

    b2 = tk.Label(root, text = '')
    b2.pack()
    ptext = tk.StringVar()
    # check_btn = tk.Button(root,text="4.Calculate Checksum",command=start)
    # check_btn.pack()
    b4 = scrolledtext.ScrolledText(root, bd=5 ,width = 60, height = 1, wrap=tk.WORD)
    b4.pack()
    
    onFinish()
    root.mainloop()