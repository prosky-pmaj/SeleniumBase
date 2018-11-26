from components.ghost.blogPage import BlogPage
from components.ghost.adminPanelPage import AdminPanelPage


class TestBlogPage(BlogPage):
    def test_01_open_blog_page(self):
        self.go_to()
        assert self.get_title() == "Blog for Testing"


class TestAdminPanelPage(AdminPanelPage):
    def test_01_open_admin_panel_page(self):
        self.go_to()
        assert self.is_log_in_required()

    def test_02_log_in_to_admin_panel(self):
        self.go_to()
        self.log_in_as_admin()
        assert not self.is_log_in_required()
        self.logOut()
