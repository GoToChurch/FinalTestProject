import pytest
from .pages.product_page import ProductPage


@pytest.mark.parametrize('slug', ['promo=offer0', 'promo=offer1', 'promo=offer2', 'promo=offer3', 'promo=offer4',
                                'promo=offer5', 'promo=offer6', pytest.param('promo=offer7', marks=pytest.mark.xfail), 'promo=offer8', 'promo=offer9'])
def test_guest_can_add_product_to_basket(browser, slug):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?{slug}"
    page = ProductPage(browser, link)
    page.open()
    page.show_current_url()
    page.add_item_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_equal_price()
    page.should_be_same_name()