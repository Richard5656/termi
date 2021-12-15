import os

print(""" ,--,                                                   
,---.'|                                                   
|   | :                                                   
:   : |     ,--,                                          
|   ' :   ,--.'|         ,---,          ,--,              
;   ; '   |  |,      ,-+-. /  |       ,'_ /|  ,--,  ,--,  
'   | |__ `--'_     ,--.'|'   |  .--. |  | :  |'. \/ .`|  
|   | :.'|,' ,'|   |   |  ,"' |,'_ /| :  . |  '  \/  / ;  
'   :    ;'  | |   |   | /  | ||  ' | |  . .   \  \.' /   
|   |  ./ |  | :   |   | |  | ||  | ' |  | |    \  ;  ;   
;   : ;   '  : |__ |   | |  |/ :  | : ;  ; |   / \  \  \  
|   ,/    |  | '.'||   | |--'  '  :  `--'   \./__;   ;  \ 
'---'     ;  :    ;|   |/      :  ,      .-./|   :/\  \ ; 
          |  ,   / '---'        `--`----'    `---'  `--`  
           ---`-'                                         
                                                         """)

print("Your system is running kernel 5.15.8")
print("Would you like to go back?")
print("Type yes to go back. Or type no to exit out of TermI")
type = input(">>>: ")

if type == 'yes':
    os.system('cd ../')
    import home.py
