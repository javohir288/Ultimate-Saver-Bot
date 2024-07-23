from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("7136595628:AAEgzXYezlelExcyMfmydL0Fm39hLfEKaA0")  # Bot toekn
ADMINS = env.list("ADMINS")  # adminlar
IP = env.str("ip")  # Xosting ip manzili






