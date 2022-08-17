import tkinter as tk

from requests import delete
from http_sender import *
from tkinter import ttk
import tkinter.messagebox

from tkinter.filedialog import askopenfilename,asksaveasfilename

font_l=('宋体',20)
font_m=('宋体',16)
font_s=('Consolas',12)

func_dict={
    "GET":sendGetRequest,
    "POST":sendPostRequest,
    "PUT":sendPutRequest,
    "DELETE":sendDeleteRequest
}

class App:
    def send_Event(self):
        send_method=self.selectBox.get()
        send_url=self.urlEntry.get()
        try:
            send_data=json.loads(self.sendArea.get(1.0,tk.END))
        except:
            tkinter.messagebox.showerror(title="error",message="发送内容必须是json格式，字符串需要加双引号！")
            return
        if send_url=="":
            tkinter.messagebox.showerror(title="error",message="url不可以为空！")
            return
        send_func=func_dict[send_method]
        ret=send_func(url=send_url,data=send_data)
        if(ret[0]==False):
            tkinter.messagebox.showerror(title="error",message="发送失败，请检查url是否正确")
            return
        else:
            self.recvArea.delete(1.0,tk.END)
            self.recvArea.insert(tk.END,ret[1])

    def selectInputFile_Event(self):
        file_type=[("json file","*.json")]
        path=askopenfilename(
            filetypes=file_type,
            defaultextension=file_type
        )
        try:
            with open(path,"r") as f:
                data=json.load(f)
                data=json.dumps(data)
        except Exception as e:
            tkinter.messagebox.showerror(title="error",message="导入失败！请检查文件！")
            return
        self.sendArea.delete(1.0,tk.END)
        self.sendArea.insert(tk.END,data)        

    def selectOutputFile_Event(self):
        file_type=[("json file","*.json")]
        path=asksaveasfilename(            
            filetypes=file_type,
            defaultextension=file_type
        )
        if not path.endswith(".json"):
            return
        try:
            with open(path,"w") as f:
                data=self.recvArea.get(1.0,tk.END)
                data=json.loads(data)
                json.dump(data,f)
        except Exception as e:
            tkinter.messagebox.showerror(title="error",message="导出失败！请检查文件！")
            return

    def __init__(self):
        #窗口
        self.window=tk.Tk()
        self.window.title('http请求测试小程序')
        self.window.geometry("800x600")
        
        #标签1
        self.label_1=tk.Label(
            master=self.window,
            font=font_l,
            text="发送内容"
        )
        self.label_1.place(x=40,y=120)
        
        #标签2
        self.label_2=tk.Label(
            master=self.window,
            font=font_l,
            text="接收内容"
        )
        self.label_2.place(x=440,y=120)

        #标签3
        self.label_3=tk.Label(
            master=self.window,
            font=font_m,
            text="选择HTTP请求类型"
        )
        self.label_3.place(x=40,y=80)        

        #标签4
        self.label_4=tk.Label(
            master=self.window,
            font=font_m,
            text="请输入URL"
        )
        self.label_4.place(x=40,y=40)             

        #单行框
        self.urlEntry=tk.Entry(
            master=self.window,
            font=font_s,
        )
        self.urlEntry.place(x=160,y=42,w=400,h=25)

        #发送框
        self.sendArea=tk.Text(
            master=self.window,
            font=font_s,
        )
        self.sendArea.place(x=40,y=160,w=320,h=400)

        #接收框
        self.recvArea=tk.Text(
            master=self.window,
            font=font_s,
        )
        self.recvArea.place(x=440,y=160,w=320,h=400)        

        #发送按键
        self.sendButton=tk.Button(
            master=self.window,
            font=font_m,
            text="发送请求",
            command=self.send_Event,            
        )
        self.sendButton.place(x=640,y=40,w=120,h=40)

        #选择文件按键
        self.inputFileButton=tk.Button(
            master=self.window,
            font=font_s,
            text="选择文件",
            command=self.selectInputFile_Event,            
        )
        self.inputFileButton.place(x=160,y=120,w=80,h=30)        

        #保存数据按键
        self.outputFileButton=tk.Button(
            master=self.window,
            font=font_s,
            text="保存数据",
            command=self.selectOutputFile_Event,            
        )
        self.outputFileButton.place(x=560,y=120,w=80,h=30)   

        #下拉列表
        self.selectBox=ttk.Combobox(
            master=self.window,
            font=font_s,
            values=['GET','POST','PUT','DELETE']
        )
        self.selectBox.current(0)
        self.selectBox.place(x=240,y=82,w=120,h=25)

if __name__=="__main__":
    app=App()
    app.window.mainloop()