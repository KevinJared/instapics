from django.test import TestCase

# Create your tests here.
class LocationTestClass(TestCase):

    def setUp(self):
        self.can = Location(image_location='Kisumu')


    def test_instance(self):
        self.assertTrue(isinstance(self.can,Location))

    def test_save_method(self):
        self.can.save_location()
        loc = Location.objects.all()
        self.assertTrue(len(loc)>0)

    def test_delete_method(self):
        self.test_location = Location(image_location='Kisumu')
        self.test_location.save_location()
        self.test_location.delete_location()
        loc = Location.objects.all()
        self.assertTrue(len(loc)<1)

    def test_update_method(self):
        self.test_location = Location(image_location='Kisumu')
        self.test_location.save_location()
        update = Location.update_location('Kisumu','Nairobi')
        self.assertTrue(update,'Nairobi')
        
class CategoryTestClass(TestCase):

    def setUp(self):
        self.space = Category(image_category='Travel')


    def test_instance(self):
        self.assertTrue(isinstance(self.space,Category))

    def test_save_method(self):
        self.space.save_category()
        space = Category.objects.all()
        self.assertTrue(len(space)>0)

    def test_delete_method(self):
        self.test_category = Category(image_category='Travel')
        self.test_category.save_category()
        self.test_category.delete_category()
        cat = Category.objects.all()
        self.assertTrue(len(cat)<1)

    def test_update_method(self):
        self.test_category = Category(image_category='Travel')
        self.test_category.save_category()
        update = Category.update_category('Travel','Movies')
        self.assertTrue(update,'Movies')
