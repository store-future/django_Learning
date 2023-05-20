from django.test import SimpleTestCase  # checking by url
from django.urls import reverse 

# Create your tests here.
class HomePageTest(SimpleTestCase):
    
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code,200)
        
    def testing_url_correct_location_byname(self):
        responce=self.client.get(reverse('home'))
        self.assertEqual(responce.status_code,200)
        
    def test_template_name_correct(self):
        response=self.client.get(reverse("home"))
        self.assertTemplateUsed(response,"home.html") # is home.html rendaring response

        
class AboutPageTest(SimpleTestCase):
    
    def test_url_available_by_name(self):
        response=self.client.get("/about/")
        self.assertEqual(response.status_code,200)
        
    def testing_url_by_name(self):
        responce=self.client.get("/about/")
        self.assertEqual(responce.status_code,200)
        


