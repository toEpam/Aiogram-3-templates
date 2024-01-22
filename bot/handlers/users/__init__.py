"""Import all routers and add them to routers_list."""
from bot.handlers.users.admin import admin_router
from bot.handlers.users.echo import echo_router
from bot.handlers.users.help import help_router
from bot.handlers.users.menu import menu_router
from bot.handlers.users.start import start_router

routers_list = [
    admin_router,
    start_router,
    help_router,
    menu_router,
    echo_router,  # echo_router must be last
]

__all__ = [
    "routers_list",
]
