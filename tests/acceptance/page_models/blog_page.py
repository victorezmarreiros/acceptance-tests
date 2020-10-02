from tests.acceptance.locators.base_page import BasePageLocators
from tests.acceptance.locators.blog_page import BlogPageLocators
from tests.acceptance.page_models.base_page import BasePage


class BlogPage(BasePage):
    @property
    def url(self):
        return super(BlogPage, self).url + '/blog'

    @property
    def posts_sections(self):
        return self.driver.find_element(*BlogPageLocators.POSTS_SECTION)

    @property
    def posts(self):
        return self.driver.find_element(*BlogPageLocators.POST)

    @property
    def add_post_link(self):
        return self.driver.find_element(*BlogPageLocators.ADD_POST_LINK)


