from aiogram import Bot, Dispatcher

from .utils.config_reader import main_settings

from .routers.reply import general_router as reply_general_router
from .routers.reply import home_router
from .routers.reply import action_router
from .routers.reply.total import total_change_router
from .routers.reply.orders import enter_id_router
from .routers.reply.orders import enter_number_router
from .routers.reply.orders import enter_count

from .routers.inline import total_count_router
from .routers.inline import append_order_router
from .routers.inline import delete_order_router
from .routers.inline import general_router as inline_general_router

from structlog.typing import FilteringBoundLogger
import structlog

logger: FilteringBoundLogger = structlog.get_logger()


async def core():
    logger.info('Credentials initialise')
    token = main_settings.token.get_secret_value()
    logger.info('Credentials initialised!')


    logger.info('Bot model initialise')
    bot = Bot(token)
    dispatcher = Dispatcher()
    logger.info('Bot model initialised!')
    
    logger.info('Routers initialise')

    logger.info('Reply routers initialise')
    dispatcher.include_router(reply_general_router.router)
    dispatcher.include_router(home_router.router)
    dispatcher.include_router(action_router.router)

    dispatcher.include_router(total_change_router.router)
    dispatcher.include_router(enter_id_router.router)
    dispatcher.include_router(enter_count.router)
    dispatcher.include_router(enter_number_router.router)
    logger.info('Reply routers initialised!')

    logger.info('Inline routers initialise')
    dispatcher.include_router(append_order_router.router)
    dispatcher.include_router(inline_general_router.router)
    dispatcher.include_router(total_count_router.router)
    dispatcher.include_router(delete_order_router.router)
    logger.info('Inline routers initialised!')

    logger.info('Routers initialised!')

    await dispatcher.start_polling(bot)