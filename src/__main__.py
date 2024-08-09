from core import core
import asyncio

from core.utils.logger_setup import get_structlog_config
from core.utils.config_reader import log_settings

from structlog.typing import FilteringBoundLogger
import structlog

logger: FilteringBoundLogger = structlog.get_logger()


async def main() -> None:
    structlog.configure(**get_structlog_config(log_settings))

    logger.info('Starting')
    await core()
    logger.info('Stopping')


if __name__ == "__main__":
    asyncio.run(main())