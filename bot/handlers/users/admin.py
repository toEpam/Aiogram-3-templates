from aiogram import Router

from bot.filters.admin import AdminFilter

admin_router = Router()
admin_router.message.filter(AdminFilter())
