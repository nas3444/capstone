import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Movie, Actor
from config import DatabaseURI

class CastingAgencyTestCase(unittest.TestCase):

    # to setup the app and initialize the db
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client

        self.database_path = DatabaseURI.SQLALCHEMY_DATABASE_URI
        
        setup_db(self.app, self.database_path)

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

    # to kill after each test
    def tearDown(self):
        pass

    #Tests - Successed

    # test for getting all movies
    def test_get_movies(self):
        res = self.client().get("/movies")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["movies"])

    # test for getting all actors
    def test_get_actors(self):
        res = self.client().get("/actors")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["actors"])

    # test for posting a new movie
    def test_post_movie(self):
        res = self.client().post("/movies", json={"title":"Testing movie", "image":"https://pbs.twimg.com/media/FHfNybWWYAEFME7.png", "release_date":"2022-02-02"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    # test for posting a new actor 
    def test_post_actor(self):
        res = self.client().post("/actors", json={"name":"Testing actor", "age":27, "gender":"male", "movie_id": 7})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    # test for patching a specific movie
    def test_patch_movie(self):
        res = self.client().post("/movies", json={"title":"Testing patch movie"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    # test for patching a specific actor
    def test_patch_actor(self):
        res = self.client().post("/actors", json={"name":"Testing patch actor"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    # test for deleting a specific movie
    def test_delete_movie(self):
        res = self.client().delete("/movies/8")
        data = json.loads(res.data)

        movie = Movie.query.get(8)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(movie, None)

    # test for deleting a specific actor
    def test_delete_actor(self):
        res = self.client().delete("/actors/8")
        data = json.loads(res.data)

        actor = Actor.query.get(8)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(actor, None)

    # Tests - failed

    # Testing case for 422 error - deleting a non existed movie
    def test_422_not_exist_movie(self):
        res = self.client().delete("/movies/40000")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unprocessable")

    # Testing case for 422 error - deleting a non existed actor
    def test_422_not_exist_actor(self):
        res = self.client().delete("/actors/900")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unprocessable")

    # Testing case for 422 error - patching a non existed movie
    def test_422_not_exist_movie(self):
        res = self.client().patch("/movies/200")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unprocessable")

    # Testing case for 422 error - patching a non existed actor
    def test_422_not_exist_actor(self):
        res = self.client().patch("/actors/200")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unprocessable")

    # Testing case for 422 error - posting an invalid movie
    def test_422_invalid_movie(self):
        res = self.client().post("/movies", json={"title": "", "image": "", "release_date":""})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unprocessable")

    # Testing case for 422 error - posting an invalid actor
    def test_422_invalid_actor(self):
        res = self.client().post("/actors", json={"name":"", "age":"", "gender":""})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unprocessable")

    # Testing case for 404 error - not found route
    def test_404_not_found(self):
        res = self.client().get("/movie")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "page not found")

    
if __name__ == "__main__":
    unittest.main()