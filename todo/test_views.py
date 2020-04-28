from django.test import TestCase
from django.shortcuts import get_object_or_404
from .models import Item

class TestViews(TestCase):
    def test_get_home_page(self):
        page = self.client.get("/")
        #This is a built in helper that will fake a request to the URL 
        #that we pass in as an argument here which is just forward slash
        #and then we can store the output of that in page.
        self.assertEqual(page.status_code, 200)
        #This will check the status code property of the page object and test that it is 200
        self.assertTemplateUsed(page, "todo_list.html")
        
    def test_get_add_item_page(self):
        page = self.client.get("/add")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "item_form.html")
    
    def test_get_edit_item_page(self):
        item = Item(name='Create a Test')
        item.save()
        # The above two lines is for the ID.
        # Once the ID has been saved django will generate an ID for it so then we will 
        # import our model
        
        page = self.client.get("/edit/{0}".format(item.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "item_form.html")
        
        # in order to pass in an ID we must first have an object in the database
        # otherwise it will fail. The view expects an ID of an actual object it can 
        # retrieve from the database.
    
    def test_get_edit_page_for_item_that_does_not_exist(self):
        page = self.client.get("/edit/1")
        self.assertEqual(page.status_code, 404)

    def test_post_create_an_item(self):
        response = self.client.post("/add", {"name": "Create a Test"})
        item = get_object_or_404(Item, pk=1)
        self.assertEqual(item.done, False)
    
    def test_post_edit_an_item(self):
        item = Item(name="Create a Test")
        item.save()
        id = item.id
        response = self.client.post("/edit/{0}".format(id), {"name": "A different name"})
        item = get_object_or_404(Item, pk=id)

        self.assertEqual("A different name", item.name)
    
    def test_toggle_status(self):
        item = Item(name="Create a Test")
        item.save()
        id = item.id
        
        response = self.client.post("/toggle/{0}".format(id))
        
        item = get_object_or_404(Item, pk=id)
        self.assertEqual(item.done, True)
    