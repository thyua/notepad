#!/usr/bin/env python
# coding: utf-8

# In[5]:


#メモ帳アプリ　保存フォルダの指定とかの実装はまだしていない

import sys
import tkinter as tk

def test():
    print('click')

root = tkinter.Tk()
root.title("メモ帳")
root.geometry("300x300")


text_widget = tk.Text(root, wrap=tk.NONE)
text_widget.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))


root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

menubar = tkinter.Menu(root)
filemenu = tkinter.Menu(menubar, tearoff=0)

# ファイルメニュー
filemenu.add_command(label="新規作成", command=test)
filemenu.add_command(label="開く", command=test)
filemenu.add_separator()
filemenu.add_command(label="保存", command=test)
filemenu.add_command(label="名前をつけて保存", command=test)
filemenu.add_command(label="閉じる", command=test)
menubar.add_cascade(label="ファイル", menu=filemenu)

# 編集メニュー
editmenu = tkinter.Menu(menubar, tearoff=0)
editmenu.add_command(label="元に戻す", command=test)
editmenu.add_separator()
editmenu.add_command(label="切り取り", command=test)
editmenu.add_command(label="コピー", command=test)
editmenu.add_command(label="貼り付け", command=test)
editmenu.add_command(label="削除", command=test)
editmenu.add_command(label="全てを選択", command=test)
menubar.add_cascade(label="編集", menu=editmenu)

root.config(menu=menubar)
root.mainloop()


