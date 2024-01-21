"""Import all routers and add them to routers_list."""
from .admin import admin_router
from .echo import echo_router
from .menu import menu_router
from .start import command_router

routers_list = [
    admin_router,
    command_router,
    menu_router,
    echo_router,  # echo_router must be last
]

__all__ = [
    "routers_list",
]
