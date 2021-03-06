"""VK tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers
# TODO: Import your custom stream types here:
from tap_vk.streams import (
    VKStream,
    AdsStream,
    AdsLayoutStream,
    AdsTargetingStream,
    CampaignsStream,
    CategoriesStream,
    StatisticsCampaignStream,
    StatisticsAdsStream
)

# TODO: Compile a list of custom stream types here
#       OR rewrite discover_streams() below with your custom logic.
STREAM_TYPES = [
    AdsStream,
    AdsLayoutStream,
    AdsTargetingStream,
    CampaignsStream,
    CategoriesStream,
    StatisticsCampaignStream,
    StatisticsAdsStream
]


class TapVK(Tap):
    """VK tap class."""
    name = "tap-vk"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "access_token",
            th.StringType,
            required=True,
            description="The token to authenticate against the API service"
        ),
        th.Property(
            "account_id",
            th.StringType,
            required=True,
            description="Идентификатор рекламного кабинета"
        ),
        th.Property(
            "client_id",
            th.StringType,
            required=True,
            description="Идентификатор клиента, у которого запрашиваются рекламные объявления."
        )
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
