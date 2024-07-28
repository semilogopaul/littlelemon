from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import menuSerializer


class MenuViewTest(TestCase):
    def test_setUp(self):
        self.client = APIClient()
        self.menu1 = Menu.objects.create(ID=4, Title='Burger', Price=7, Inventory=9)
        self.menu2 = Menu.objects.create(ID=5, Title='Falafel', Price=8, Inventory=15)
        self.menu3 = Menu.objects.create(ID=6, Title='Lasagma', Price=9, Inventory=13)

    def test_getall(self):
        response = self.client.get('/menu/')
        menus = Menu.objects.all()
        serializer = menuSerializer(menus, many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)