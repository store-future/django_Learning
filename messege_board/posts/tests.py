from django.test import TestCase
from .models import Post
from django.urls import reverse

'''
1- postdata = setting up test data  and then check that it is stored correctly in the database.
2- only function start with test name will execute adn show
'''

class PostTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):                  # cloning our Post database and name it post then assigning text column to it  
        cls.post=Post.objects.create(text="this is a test")       
        
    def test_model_content(self):
        self.assertEqual(self.post.text,"this is a test")    
        
    def test_url_exists_at_correct_location(self):
        response=self.client.get("/")
        self.assertEqual(response.status_code,200)
        
    def test_homepage(self):
       response = self.client.get(reverse("home"))
       self.assertEqual(response.status_code,200)      #testing whether url available by name
       self.assertTemplateUsed(response,"home.html")   # testing whether template used correct name
       