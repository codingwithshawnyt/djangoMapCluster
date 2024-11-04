from django.test import TestCase

# Basic test cases for the anymap views

class ViewTests(TestCase):
    def test_home_view_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_leaflet_view_status_code(self):
        response = self.client.get('/leaflet/')
        self.assertEqual(response.status_code, 200)

    def test_google_view_status_code(self):
        response = self.client.get('/google/')
        self.assertEqual(response.status_code, 200)

    def test_openlayers_view_status_code(self):
        response = self.client.get('/openlayers/')
        self.assertEqual(response.status_code, 200)
