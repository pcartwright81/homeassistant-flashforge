from homeassistant.helpers.entity import Entity
from .const import DOMAIN

class FlashforgeEntity(Entity):
    """Representation of a Flashforge entity."""

    _attr_has_entity_name = True

    def __init__(self, coordinator, config_entry):
        """Initialize the entity."""
        self.coordinator = coordinator
        self.config_entry = config_entry
        self._attr_device_info = {
            "identifiers": {(DOMAIN, config_entry.entry_id)},
            "name": "Flashforge 3D Printer",
            "manufacturer": "FlashForge",
        }

    @property
    def available(self) -> bool:
        """Return if entity is available."""
        return self.coordinator.last_update_success

    async def async_update(self) -> None:
        """Update the entity."""
        await self.coordinator.async_request_refresh()
