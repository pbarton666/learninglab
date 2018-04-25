# -*- coding: utf-8 -*-
"""Experimenting with Japanese programming"""

#NB to get this to play well with Wing, set encoding to UTF-8
#      Edit.. Preferences..Debugger..IO

#use assign a new name to a built-in function
刷る =  print          #"tsuru"

#create a standard python object
翻訳家 = {                     #translator "hanyakuka"
    "アードバーク" : 'aardvark',  #"addobakku"
    "にしきへび"  : 'python',     #"nishichi hebi"
    "日本"      : 'Japan' ,    #"nihon"
}

#create a function (need to use the keyword in English)
def 自分を刷る(単語):                #print_me(word)                 "watashi wo tsuru (tango)"
    刷る(単語, 翻訳家[単語])         #print(word, <translation>)     "tsuru(tango)" 

#call the function with an argument
単語 = "アードバーク"       #word = aadvark  "tango ikoru addobakku""
自分を刷る(単語)

単語 = "にしきへび"      #word = python   "tango ikoru nishichi hebi"
自分を刷る(単語)

刷る()
刷る('終わりんこ! (done!)')       #print('done')   "tsuru(orarinko)"
