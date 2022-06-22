"""Stream type classes for tap-vk."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_vk.client import VKStream

# TODO: Delete this is if not using json files for schema definition
SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class AdsStream(VKStream):
    """Define custom stream."""

    name = "ads"
    path = "/ads.getAds"
    primary_keys = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property(
            "id",
            th.IntegerType,
        ),
        th.Property("campaign_id", th.IntegerType),
        th.Property("status", th.IntegerType),
        th.Property("approved", th.IntegerType),
        th.Property("create_time", th.IntegerType),
        th.Property("update_time", th.IntegerType),
        th.Property("goal_type", th.IntegerType),
        th.Property("cost_type", th.IntegerType),
        th.Property("day_limit", th.StringType),
        th.Property("all_limit", th.StringType),
        th.Property("start_time", th.IntegerType),
        th.Property("stop_time", th.IntegerType),
        th.Property("category1_id", th.IntegerType),
        th.Property("category2_id", th.IntegerType),
        th.Property("age_restriction", th.IntegerType),
        th.Property("name", th.StringType),
        th.Property(
            "events_retargeting_groups", th.StringType
        ),
        th.Property("conversion_pixel_id", th.IntegerType),
        th.Property("conversion_event_id", th.IntegerType),
        th.Property("ad_format", th.IntegerType),
        th.Property("ocpm", th.StringType),
        th.Property("ad_platform", th.StringType),
        th.Property("publisher_platforms", th.StringType),
        th.Property("publisher_platforms_auto", th.IntegerType),
        th.Property("autobidding", th.IntegerType),
        th.Property("has_campaign_budget_optimization", th.BooleanType),
    ).to_dict()

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        params = super().get_url_params(context, next_page_token)
        params["include_deleted"] = 1
        return params


class AdsLayoutStream(VKStream):
    """Define custom stream."""

    name = "ads_layout"
    path = "/ads.getAdsLayout"
    primary_keys = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property(
            "id",
            th.IntegerType,
        ),
        th.Property("campaign_id", th.IntegerType),
        th.Property("goal_type", th.IntegerType),
        th.Property("cost_type", th.IntegerType),
        th.Property("age_restriction", th.IntegerType),
        th.Property("title", th.StringType),
        th.Property("link_type", th.IntegerType),
        th.Property("link_url", th.StringType),
        th.Property("link_domain", th.StringType),
        th.Property("ad_format", th.IntegerType),
        th.Property("preview_link", th.StringType),
        th.Property("image_src", th.StringType),
        th.Property("hide_likes", th.BooleanType),
    ).to_dict()

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        params = super().get_url_params(context, next_page_token)
        params["include_deleted"] = 1
        return params


class AdsTargetingStream(VKStream):
    """Define custom stream."""

    name = "ads_targeting"
    path = "/ads.getAdsTargeting"
    primary_keys = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property(
            "id",
            th.IntegerType,
        ),
        th.Property("campaign_id", th.IntegerType),
        th.Property("sex", th.StringType),
        th.Property("age_from", th.StringType),
        th.Property("age_to", th.StringType),
        th.Property("country", th.StringType),
        th.Property("groups_recommended", th.StringType),
        th.Property("cities", th.StringType),
        th.Property("key_phrases", th.StringType),
        th.Property("groups_formula", th.StringType),
        th.Property("groups_active_recommended", th.StringType),
        th.Property("interest_categories_formula", th.StringType),
        th.Property("retargeting_groups", th.StringType),
        th.Property("price_list_audience_type", th.StringType),
        th.Property("key_phrases_days", th.StringType),
        th.Property("count", th.StringType),
    ).to_dict()

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        params = super().get_url_params(context, next_page_token)
        params["include_deleted"] = 1
        return params


class CampaignsStream(VKStream):
    """Define custom stream."""

    name = "campaigns"
    path = "/ads.getCampaigns"
    primary_keys = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property(
            "id",
            th.IntegerType,
        ),
        th.Property("status", th.IntegerType),
        th.Property("create_time", th.IntegerType),
        th.Property("update_time", th.IntegerType),
        th.Property("goal_type", th.IntegerType),
        th.Property("day_limit", th.StringType),
        th.Property("all_limit", th.StringType),
        th.Property("start_time", th.IntegerType),
        th.Property("stop_time", th.IntegerType),
        th.Property("name", th.StringType),
        th.Property(
            "type", th.StringType
        ),
        th.Property("user_goal_type", th.IntegerType),
        th.Property("views_limit", th.IntegerType),
        th.Property("is_cbo_enabled", th.BooleanType),
    ).to_dict()

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        params = super().get_url_params(context, next_page_token)
        params["include_deleted"] = 1
        return params