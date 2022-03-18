import easygui as eg

height = eg.integerbox(msg="请输入身高(cm)", title="身高计算器", default=None,
               lowerbound=0, upperbound=10000, image=None, root=None)
eg.msgbox(msg="您的身高是"+str(height)+"cm",title="身高计算器",
           ok_button="屑屑你")
