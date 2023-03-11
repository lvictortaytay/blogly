from app import app
from unittest import TestCase





class testApp(TestCase):
    def test_homePage(self):
        with app.test_client() as client:
            resp = client.get("/")
            html = resp.get_data(as_text = True)

            self.assertEqual(resp.status_code,200)

    
    def test_addUserPage(self):
        with app.test_client() as client:
            resp = client.get("/addUser")
            html = resp.get_data(as_text = True)

            self.assertEqual(resp.status_code ,200)
            self.assertIn("create a user!", html)


    def test_createUserPage(self):
        with app.test_client() as client:
            res = client.post("/createUser" , data = {"firstName" : "lvictor" , "lastName" : "taylor" , "imageUrl" : "https://inman-murphy.com/wp-content/uploads/roachcontrol.jpeg"})
            

            self.assertEqual(res.status_code,302)
            self.assertEqual(res.location , "http://localhost/")


    def test_homeAddBtn(self):
        with app.test_client() as client:
            res = client.get("/")
            html = res.get_data(as_text = True)


            self.assertEqual(res.status_code , 200)
            self.assertIn("Users!" , html)


        