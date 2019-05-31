# AlwaysOnline™

Keep your Telegram Always Online.
让你的 Telegram 永远"在线"

使用了开源项目 - Many Thanks to project: https://github.com/LonamiWebs/Telethon/

# 背景

Don't let others peak on your daily routine with recent online! So keep yourself always online. XD  
如果你不想被人通过在线时间判断作息规律，那就让自己一直保持在线吧！  
（这样子就算你让所有人看见你的在线时间也无所谓咯，同时你还可以看到别人的）  

# 需求 Prerequisite

`PYTHON3`  
`一台可以连接到Telegram的服务器`  

需要包：`Telethon`  
使用这个指令直接安装到全局 | Install package globally with ：`pip3 install telethon==0.19.1.6`  

# 如何使用？ How to use

- 首先，你需要一个 `Client Token`(这个可以在 https://my.telegram.org 申请)
    - 教程：https://github.com/NeverBehave/AlwaysOnline-/blob/master/%E8%AF%B4%E6%98%8E%E6%96%87%E6%A1%A3/%E5%A6%82%E4%BD%95%E7%94%B3%E8%AF%B7Client%20Token.md
- `git clone https://github.com/NeverBehave/AlwaysOnline-` 或者下载压缩包解压
- 将 `api_id` 和 `api_hash` 填入 `data.py` 适当的位置
    - Fill in your id and hash @ `data.py`
- `python3 main.py`
- 按照指引完成登录
    - Follow the instruction and you are good to go !

# 提示 Tips

- 不要在**不安全**的地方部署这个脚本，妥善地保管好目录下的`Session`文件，否则相当于给予**任何人访问你的账号的权限** 
    - Take good care of the `session` file under this directory, or your account will be at risk.
- 这个脚本不会使你的消息变为已读，你不会在日常使用中察觉到脚本的存在
    - You can still use your account normally. Nothing else will change (Message count, etc.).
     

# 原理 How it works

Send an online status message to Telegram periodically. Your actions are not necessary change your online status.  
间歇性的给 Telegram 发送你在线的信息，实际上你发送信息并不意味着你上线，只有你主动改变了你的状态  
How weird Telegram API is.  
这就是为什么 Telegram 的 API 很奇怪  
