from django.test import SimpleTestCase
from django.urls import reverse, resolve
from receipts_organizer.views import (
    CategoryList, CategoryDetails, NewCategory, EditCategory, DeleteCategory,
    EntryList, EntryDetail, EditEntry, NewEntry, DeleteEntry, MyPage
)


class TestUrls(SimpleTestCase):
    """
    Test all urls in receipts organizer app
    These test has been inspired by 
    'The Dumbfonds' youtube video on django testing
    """
    def test_mypage_url_resolves(self):
        """
        Test url for new entry page
        """
        url = reverse('mypage')
        self.assertEqual(resolve(url).func.view_class, MyPage)

    def test_categories_url_resolves(self):
        """
        Test url for categories page
        """
        url = reverse('categories')
        self.assertEqual(resolve(url).func.view_class, CategoryList)

    def test_category_detail_url_resolves(self):
        """
        Test url for categories detail page
        """
        url = reverse('detail_category', args=[3])
        self.assertEqual(resolve(url).func.view_class, CategoryDetails)

    def test_new_category_url_resolves(self):
        """
        Test url for new category page
        """
        url = reverse('new_category')
        self.assertEqual(resolve(url).func.view_class, NewCategory)

    def test_edit_category_url_resolves(self):
        """
        Test url for edit category page
        """
        url = reverse('edit_category', args=[21])
        self.assertEqual(resolve(url).func.view_class, EditCategory)

    def test_delete_category_url_resolves(self):
        """
        Test url for delete category page
        """
        url = reverse('delete_category', args=[320])
        self.assertEqual(resolve(url).func.view_class, DeleteCategory)

    def test_entires_url_resolves(self):
        """
        Test url for entries page
        """
        url = reverse('entries')
        self.assertEqual(resolve(url).func.view_class, EntryList)

    def test_entiry_detail_url_resolves(self):
        """
        Test url for entry detail page
        """
        url = reverse('entry_detail', args=[5])
        self.assertEqual(resolve(url).func.view_class, EntryDetail)

    def test_new_entry_url_resolves(self):
        """
        Test url for new entry page
        """
        url = reverse('new_entry')
        self.assertEqual(resolve(url).func.view_class, NewEntry)

    def test_edit_entry_url_resolves(self):
        """
        Test url for edit entry page
        """
        url = reverse('edit_entry', args=[43])
        self.assertEqual(resolve(url).func.view_class, EditEntry)

    def test_delete_entry_url_resolves(self):
        """
        Test url for delete entry page
        """
        url = reverse('delete_entry', args=[57])
        self.assertEqual(resolve(url).func.view_class, DeleteEntry)
