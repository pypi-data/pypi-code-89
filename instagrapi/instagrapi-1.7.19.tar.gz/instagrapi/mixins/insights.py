import time
from typing import Dict, List

from instagrapi.exceptions import ClientError, MediaError, UserError
from instagrapi.utils import json_value


class InsightsMixin:
    """
    Helper class to get insights
    """

    def insights_media_feed_all(
        self,
        post_type: str = "ALL",
        time_frame: str = "TWO_YEARS",
        data_ordering: str = "REACH_COUNT",
        count: int = 0,
        sleep: int = 2,
    ) -> List[Dict]:
        """
        Get insights for all medias from feed with page iteration with cursor and sleep timeout

        Parameters
        ----------
        post_type: str, optional
            Types of posts, default is "ALL"
            Options: ("ALL", "CAROUSEL_V2", "IMAGE", "SHOPPING", "VIDEO")
        time_frame: str, optional
            Time frame to pull media insights, default is "TWO_YEARS"
            Options: ("ONE_WEEK", "ONE_MONTH", "THREE_MONTHS", "SIX_MONTHS", "ONE_YEAR", "TWO_YEARS")
        data_ordering: str, optional
            Ordering strategy for the data, default is "REACH_COUNT"
            Options: ("REACH_COUNT", "LIKE_COUNT", "FOLLOW", "SHARE_COUNT", "BIO_LINK_CLICK", "COMMENT_COUNT", "IMPRESSION_COUNT", "PROFILE_VIEW", "VIDEO_VIEW_COUNT", "SAVE_COUNT"...)
        count: int, optional
            Max media count for retrieving, default is 0
        sleep: int, optional
            Timeout between pages iterations, default is 2

        Returns
        -------
        List[Dict]
            List of dictionaries of response from the call
        """
        assert self.user_id, "Login required"
        supported_post_types = ("ALL", "CAROUSEL_V2", "IMAGE", "SHOPPING", "VIDEO")
        supported_time_frames = (
            "ONE_WEEK",
            "ONE_MONTH",
            "THREE_MONTHS",
            "SIX_MONTHS",
            "ONE_YEAR",
            "TWO_YEARS",
        )
        assert post_type in supported_post_types, "Unsupported post type"
        assert time_frame in supported_time_frames, "Unsupported time frame"

        medias = []
        cursor = None
        data = {
            "surface": "post_grid",
            "doc_id": 2345520318892697,
            "locale": "en_US",
            "vc_policy": "insights_policy",
            "strip_nulls": False,
            "strip_defaults": False,
        }
        query_params = {
            "IgInsightsGridMediaImage_SIZE": 480,
            "count": 200,  # TODO Try to detect max allowed value
            # "cursor": "0",
            "dataOrdering": data_ordering,
            "postType": post_type,
            "timeframe": time_frame,
            "search_base": "USER",
            "is_user": "true",
            "queryParams": {"access_token": "", "id": self.user_id},
        }
        while True:
            if cursor:
                query_params["cursor"] = cursor

            result = self.private_request(
                "ads/graphql/",
                self.with_query_params(data, query_params),
            )
            if not json_value(
                result,
                "data",
                "shadow_instagram_user",
                "business_manager",
                default=None,
            ):
                raise UserError("Account is not business account", **self.last_json)

            stats = result["data"]["shadow_instagram_user"]["business_manager"][
                "top_posts_unit"
            ]["top_posts"]
            cursor = stats["page_info"]["end_cursor"]
            medias.extend(stats["edges"])
            if not stats["page_info"]["has_next_page"]:
                break
            if count and len(medias) >= count:
                break
            time.sleep(sleep)
        if count:
            medias = medias[:count]
        return medias

    """
    Helpers for getting insights for media
    """

    def insights_account(self) -> Dict:
        """
        Get insights for account

        Returns
        -------
        Dict
            A dictionary of response from the call
        """
        assert self.user_id, "Login required"
        data = {
            "surface": "account",
            "doc_id": 2449243051851783,
            "locale": "en_US",
            "vc_policy": "insights_policy",
            "strip_nulls": False,
            "strip_defaults": False,
        }
        query_params = {
            "IgInsightsGridMediaImage_SIZE": 360,
            "activityTab": True,
            "audienceTab": True,
            "contentTab": True,
            "query_params": {"access_token": "", "id": self.user_id},
        }

        result = self.private_request(
            "ads/graphql/",
            self.with_query_params(data, query_params),
        )
        res = json_value(result, "data", "shadow_instagram_user", "business_manager")
        if not res:
            raise UserError("Account is not business account", **self.last_json)
        return res

    def insights_media(self, media_pk: int) -> Dict:
        """
        Get insights data for media

        Parameters
        ----------
        media_pk: int
            PK for the album you want to download

        Returns
        -------
        Dict
            A dictionary with insights data
        """
        assert self.user_id, "Login required"
        media_pk = self.media_pk(media_pk)
        data = {
            "surface": "post",
            "doc_id": 3221905377882880,
            "locale": "en_US",
            "vc_policy": "insights_policy",
            "strip_nulls": False,
            "strip_defaults": False,
        }
        query_params = {
            "query_params": {"access_token": "", "id": media_pk},
        }
        try:
            result = self.private_request(
                "ads/graphql/",
                self.with_query_params(data, query_params),
            )
            return result["data"]["instagram_post_by_igid"]
        except ClientError as e:
            raise MediaError(e.message, media_pk=media_pk, **self.last_json)
