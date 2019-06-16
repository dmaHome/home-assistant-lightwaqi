"""
Light support for the World Air Quality Index service only usable with station index.
It has also only be tested with stations located in France.

"""
import asyncio
import logging
from datetime import timedelta

import aiohttp
import voluptuous as vol

from homeassistant.exceptions import PlatformNotReady
import homeassistant.helpers.config_validation as cv
from homeassistant.const import (
    ATTR_ATTRIBUTION, ATTR_TIME, CONF_TOKEN)
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.config_validation import PLATFORM_SCHEMA
from homeassistant.helpers.entity import Entity

VERSION = '1.0.0'

_LOGGER = logging.getLogger(__name__)

ATTR_DOMINENTPOL = 'dominentpol'
ATTR_NITROGEN_DIOXIDE = 'nitrogen_dioxide'
ATTR_OZONE = 'ozone'
ATTR_PM10 = 'pm_10'
ATTR_PM2_5 = 'pm_2_5'
ATTR_SULFUR_DIOXIDE = 'sulfur_dioxide'
ATTR_CARBON_MONOXIDE = 'carbon_monoxide'

KEY_TO_ATTR = {
    'pm25': ATTR_PM2_5,
    'pm10': ATTR_PM10,
    'o3': ATTR_OZONE,
    'no2': ATTR_NITROGEN_DIOXIDE,
    'so2': ATTR_SULFUR_DIOXIDE,
    'co' : ATTR_CARBON_MONOXIDE,
}

ATTRIBUTION = 'Data provided by the World Air Quality Index project'

CONF_STATIONS = 'stations'

SCAN_INTERVAL = timedelta(minutes=5)

TIMEOUT = 10

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Optional(CONF_STATIONS): cv.ensure_list,
    vol.Required(CONF_TOKEN): cv.string,
})



async def async_setup_platform(hass, config, async_add_entities,
                               discovery_info=None):
    """Set up the requested World Air Quality Index locations."""
    import waqiasync

    token = config.get(CONF_TOKEN)
    stations = config.get(CONF_STATIONS)

    client = waqiasync.WaqiClient(
        token, async_get_clientsession(hass), timeout=TIMEOUT)
    dev = []
    try:
        for station_id in stations:
            station = await client.get_station_by_number(station_id)
            _LOGGER.debug("The following station was returned: %s", station)
            waqi_sensor = WaqiSensor(client, station)
            if {waqi_sensor.idx,
                waqi_sensor.station_name}:
                dev.append(waqi_sensor)
    except (aiohttp.client_exceptions.ClientConnectorError,
            asyncio.TimeoutError):
        _LOGGER.exception('Failed to connect to WAQI servers.')
        raise PlatformNotReady
    async_add_entities(dev, True)


class WaqiSensor(Entity):
    """Implementation of a WAQI sensor."""

    def __init__(self, client, station):
        """Initialize the sensor."""
        self._client = client
        try:
            self.idx = station['idx']
        except (KeyError, TypeError):
            self.idx = None

        try:
            self.station_name = station['station']['name']
        except (KeyError, TypeError):
            try:
                self.station_name = station['city']['name']
            except (KeyError, TypeError):
                self.station_name = None

        self._data = None

    @property
    def name(self):
        """Return the name of the sensor."""
        if self.station_name:
            return 'WAQI {}'.format(self.station_name)
        return 'WAQI {}'.format(self.idx)

    @property
    def icon(self):
        """Icon to use in the frontend, if any."""
        return 'mdi:air-purifier'

    @property
    def state(self):
        """Return the state of the device."""
        if self._data is not None:
            return self._data.get('aqi')
        return None

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement of this entity, if any."""
        return 'AQI'

    @property
    def device_state_attributes(self):
        """Return the state attributes of the last update."""
        attrs = {}

        if self._data is not None:
            try:
                attrs[ATTR_ATTRIBUTION] = ' and '.join(
                    [ATTRIBUTION] + [
                        v['name'] for v in self._data.get('attributions', [])])

                attrs[ATTR_TIME] = self._data['time']['s']
                attrs[ATTR_DOMINENTPOL] = self._data.get('dominentpol')

                iaqi = self._data['iaqi']
                for key in iaqi:
                    if key in KEY_TO_ATTR:
                        attrs[KEY_TO_ATTR[key]] = iaqi[key]['v']
                    else:
                        attrs[key] = iaqi[key]['v']
                return attrs
            except (IndexError, KeyError):
                return {ATTR_ATTRIBUTION: ATTRIBUTION}

    async def async_update(self):
        """Get the latest data and updates the states."""
        if self.idx:
            result = await self._client.get_station_by_number(self.idx)
        else:
            result = None
        self._data = result
