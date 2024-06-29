import os
from pyrogram import Client

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6284624690:AAHPsLhYyQs25Y78pbQjgIsgzG7oqTcUQtM")
API_HASH = os.environ.get("API_HASH", "c23db4aa92da73ff603666812268597a")
API_ID = os.environ.get("API_ID", 2374174)
MUBI_TOKEN = "643dfc8eee88d0147244cb05bd9f2f02bb834b"
MUBI_BEARER = "eyJ1c2VySWQiOjEyMjg4ODQzLCJzZXNzaW9uSWQiOiI2NDNkZmM4ZWVlODhkMDE0NzI0NGNiMDViZDlmMmYwMmJiODM0YiIsIm1lcmNoYW50IjoibXViaSJ9"
OWNER_ID = os.environ.get("OWNER_ID", "mmagneto")
STREAMTAPE_API_PASS="lW3WyaGz9rh7ko7"
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001947056140"))
POSTA = "gncrali2006@gmail.com"
PASS = "Gncrali2006"
CAP = "true"
STREAMTAPE_API_USERNAME="041db6b5ed20e4d5816b"
STRING_SESSION = os.environ.get('STRING_SESSION', 'BACVj_JzS6Sqgnq754w8mbemtrHhrQAJfAtxzUsjcifzTzETUknZd1T25wP8ZRrIMsmKDxQDtSW3xlj7MXFrrZSuGxxyzaH3_bUXhCZP-5s4ZkcA87nWCUsEGSO96lkj3s3xa5sVTMXI7C6bA2Tv9kUGxRIjUCg810cx4dr9o9PrEWfKnzrW7F0yia2UbyNz_gyo1L3Jqtuy3LEG77LpydMOUtzAgmw3AUIyKsF2U6nF3ICf7lKp_baXnsEtDeBNiORqgRS0nxC5OxhdeSoBitJy3w7Lr5QfoUn39eIAag2vSu7f06QGrIVWOHVNKrefpFgaN1qjw3-O6J9ckbvLGZo1X19oqAA')
if len(STRING_SESSION) != 0:
    try:
        userbot = Client(
            name='Userbot',
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=STRING_SESSION,
        ) 
        userbot.start()
        me = userbot.get_me()
        userbot.send_message(OWNER_ID, f"Userbot Bașlatıldı..\n\n**Premium Durumu**: {me.is_premium}\n**Ad**: {me.first_name}\n**id**: {me.id}")
        print("Userbot Başlatıldı..")
    except Exception as e:
        print(e)
