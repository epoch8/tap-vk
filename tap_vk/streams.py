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

    def get_child_context(self, record: dict, context: Optional[dict]) -> dict:
        """Return a context dictionary for child streams."""
        return {
            "ad_id": record["id"],
        }


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
        th.Property("type", th.StringType),
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

    def get_child_context(self, record: dict, context: Optional[dict]) -> dict:
        """Return a context dictionary for child streams."""
        return {
            "campaign_id": record["id"],
        }


class CategoriesStream(VKStream):
    """Define custom stream."""

    name = "categories"
    path = "/ads.getCategories"
    records_jsonpath = "$[response][v2][*]"
    primary_keys = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property(
            "id",
            th.IntegerType,
        ),
        th.Property("name", th.StringType),
        th.Property(
            "subcategories",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.IntegerType),
                    th.Property("name", th.StringType),
                )
            ),
        ),
    ).to_dict()

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        params = super().get_url_params(context, next_page_token)
        params["lang"] = "en"
        return params


class StatisticsCampaignStream(VKStream):
    """Define custom stream."""

    name = "statistics_campaign"
    parent_stream_type = CampaignsStream
    path = "/ads.getStatistics"
    primary_keys = ["id"]
    replication_key = None

    schema = th.PropertiesList(
        th.Property(
            "id",
            th.IntegerType,
        ),
        th.Property("type", th.StringType),
        th.Property(
            "stats",
            th.ArrayType(
                th.ObjectType(
                    th.Property("day", th.StringType),
                    th.Property("month", th.StringType),
                    th.Property("overall", th.IntegerType),
                    th.Property("spent", th.NumberType),
                    th.Property("impressions", th.StringType),
                    th.Property("clicks", th.IntegerType),
                    th.Property("reach", th.IntegerType),
                    th.Property("join_rate", th.IntegerType),
                    th.Property("link_external_clicks", th.IntegerType),
                    th.Property("ctr", th.NumberType),
                    th.Property("uniq_views_count", th.IntegerType),
                    th.Property("effective_cost_per_click", th.NumberType),
                    th.Property("effective_cost_per_mille", th.NumberType),
                    th.Property("effective_cpf", th.NumberType),
                )
            ),
        ),
    ).to_dict()

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        params = super().get_url_params(context, next_page_token)
        params["ids_type"] = "campaign"
        params["period"] = "day"
        params["date_from"] = "2022-01-01"
        params["date_to"] = "2022-06-22"
        params["ids"] = context["campaign_id"]
        return params


class StatisticsAdsStream(VKStream):
    """Define custom stream."""

    name = "statistics_ads"
    parent_stream_type = AdsStream
    path = "/ads.getStatistics"
    primary_keys = ["id"]
    replication_key = None

    schema = th.PropertiesList(
        th.Property(
            "id",
            th.IntegerType,
        ),
        th.Property("type", th.StringType),
        th.Property(
            "stats",
            th.ArrayType(
                th.ObjectType(
                    th.Property("day", th.StringType),
                    th.Property("month", th.StringType),
                    th.Property("overall", th.IntegerType),
                    th.Property("spent", th.NumberType),
                    th.Property("impressions", th.StringType),
                    th.Property("clicks", th.IntegerType),
                    th.Property("reach", th.IntegerType),
                    th.Property("join_rate", th.IntegerType),
                    th.Property("link_external_clicks", th.IntegerType),
                    th.Property("ctr", th.NumberType),
                    th.Property("uniq_views_count", th.IntegerType),
                    th.Property("effective_cost_per_click", th.NumberType),
                    th.Property("effective_cost_per_mille", th.NumberType),
                    th.Property("effective_cpf", th.NumberType),
                )
            ),
        ),
    ).to_dict()

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        params = super().get_url_params(context, next_page_token)
        params["ids_type"] = "ad"
        params["period"] = "day"
        params["date_from"] = "2022-01-01"
        params["date_to"] = "2022-06-22"
        params["ids"] = context["ad_id"]
        return params
