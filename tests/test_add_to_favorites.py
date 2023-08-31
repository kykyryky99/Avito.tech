import pytest

from pages.ad_page import AdPage


def check_favorite(id_ad: int) -> bool:
    ad_page = AdPage(id_ad=id_ad)
    ad_page.call_button_add_favorites()
    ad_page.call_button_my_favorites()
    is_find = ad_page.find_ad_after_add()

    return is_find


@pytest.mark.parametrize(
    "id_ad",
    [
        2639542363,
    ]
)
def test_add_to_favorites_from_ads(id_ad: int):
    complete = check_favorite(id_ad)
    if complete is False:
        raise AssertionError(f"Ad {id_ad} not added to favorites")



