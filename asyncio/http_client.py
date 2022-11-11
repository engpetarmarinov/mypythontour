import asyncio
import logging
import aiohttp


class HttpClient:
    def _get_connector(self):
        if hasattr(self, "_connector") and self._connector is not None:
            return self._connector

        self._connector = aiohttp.TCPConnector(
            limit=0,
            limit_per_host=0,
            ssl=False,
            use_dns_cache=True,
            ttl_dns_cache=10800,
        )

        return self._connector

    async def get_url_async(self, url):
        try:
            async with aiohttp.ClientSession(connector=self._get_connector(), connector_owner=False) as session:
                async with session.get(url) as resp:
                    return resp
        except asyncio.CancelledError:
            logging.WARNING(f"{url} cancelled")

    def __del__(self):
        if hasattr(self, "_connector") and self._connector is not None:
            self._connector.close()
