import asyncio
import logging

from flashforge_python_api import FlashforgeAPI
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)


class FlashforgeCoordinator(DataUpdateCoordinator):
    """Flashforge coordinator."""

    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None:
        """Initialize the coordinator."""
        self.entry = entry
        self.api = FlashforgeAPI(entry.data["host"], entry.data["username"], entry.data["password"])
        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_method=self._async_update_data,
            update_interval=entry.data.get("update_interval", 30),
        )

    async def _async_update_data(self):
        """Fetch data from API."""
        try:
            return await self.api.get_status()
        except Exception as err:
            _LOGGER.error("Error communicating with Flashforge API: %s", err)
            raise
