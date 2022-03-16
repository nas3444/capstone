import os
SECRET_KEY = os.urandom(32)

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

# create the database uri


class DatabaseURI:
    DATABASE_NAME = 'capstone'
    username = 'postgres'
    password = 'root'
    url = 'localhost:5432'
    # SQLALCHEMY_DATABASE_URI = "postgresql://{}:{}@{}/{}".format(
    # username, password, url, DATABASE_NAME)
    SQLALCHEMY_DATABASE_URI = "postgresql://werstburlgekgx:542ee72151d25e995c7aea35dc755b1f8a458f8c437527706c1041105ee366f8@ec2-34-230-110-100.compute-1.amazonaws.com:5432/dac1qdvhrqukb4"


assistant_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImphS1R3TFljZHNkUl9ZZVlzcXlJOSJ9.eyJpc3MiOiJodHRwczovL2Rldi1kejk1ZXVkcS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjFmZmM5YWViNTE1ZTkwMDcwNWUxODA1IiwiYXVkIjoiY2FzdGluZyIsImlhdCI6MTY0NzI0OTczOCwiZXhwIjoxNjQ3MjY3NzM4LCJhenAiOiJ1NWtxVXAyY1N5eHludVV0SERQRndIaVNtUFpyZ3lzWCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.wVQtl2Gla1JtVpjYkCRG3LeFDZkr9VcuUcXNK491lnCJ1m1Gb8vpJihECiI_AQGBV7MEmCNfMaBTalUNXZGBTZCiMaUlktDbklEXjC6A3LFisdFZWNHtr8TaVhgi0YNSI9_q6MU9jbh1lZDFLFZIEvzMqqNOr0IRg9fhliFQE6vUpMAtNckpkxGwg-4qnMeRjbDlD4pIhixoCLWXSUqFxs3LOGi_OaeY9BvTX4duLa2XBo6smS5i_MlSpv171U6llR8OzewF3SvaLrFcpSVP3PZsdNNNzgdQVUQiMKuEadmRvqvTjv_h8tD-nLkXxQTdhf85gAaLDNDBG5hxIRO10A"
director_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImphS1R3TFljZHNkUl9ZZVlzcXlJOSJ9.eyJpc3MiOiJodHRwczovL2Rldi1kejk1ZXVkcS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjFmZmM5ZGZhYWUxMTgwMDY5ZmQxOTI0IiwiYXVkIjoiY2FzdGluZyIsImlhdCI6MTY0NzI0OTgwMiwiZXhwIjoxNjQ3MjY3ODAyLCJhenAiOiJ1NWtxVXAyY1N5eHludVV0SERQRndIaVNtUFpyZ3lzWCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiXX0.Ihig75aaGGPVsBnTnqiI6I19N3ES7eL8rKIkKCdMetSfAH5Y9dycthTxhLkFTO3d1ok0X6wwrH0g1upPuZV_oTrBgPf0AnhmI4sda7YM2nlOFpEzzLEFX8FFEwcZFRXvsp0GyhKXRHIoIyFX2H98wzUxyGRosOmsDDRinPiUymasQwKQJMIG8UfI4rIYZXm7BEDOovViuazemgq4CMn_GfD9zfQW2QUMGnS3LlHAoVRjM66Bez_KuXC0Q1KsuUUXfqo5oesM3ZBoIeR-ioiJsauerJ5SsllHwkCOmJsTDPmv_FnEeH0f9YCdqA6gDMZ1AHnQ7r02SwSX4-Do8ajfcA"
producer_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImphS1R3TFljZHNkUl9ZZVlzcXlJOSJ9.eyJpc3MiOiJodHRwczovL2Rldi1kejk1ZXVkcS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjFmNzk1MzYzMWE1N2YwMDY4ZTQwMmQ2IiwiYXVkIjoiY2FzdGluZyIsImlhdCI6MTY0NzI0OTg2NCwiZXhwIjoxNjQ3MjY3ODY0LCJhenAiOiJ1NWtxVXAyY1N5eHludVV0SERQRndIaVNtUFpyZ3lzWCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.v8iQQSyVs21SiZZ6yGHZ9irY1_P3b4aglwKT0fUfqnNwAv1vpOxelPGG8jhjW8bMQVrpRgdBaIsNedNopR5Q5VWRLxKUhT7iNmKqx7NGXi85yz7zkKhTOl4rD0C1ISdCKlPAL0h6UvZjPK-l08bPyEyO0Plis5Wi6yQHNzQE-iOCzwJUenzzUyWO0ST1de03ssIbuzsnsgLotxadiWvwmxO1Ekibc-n1vRl5-4dpYVixk1bmLWmnCUKeq3n-eTRlHSlc3sATGerXeaTASUarbOaZE_h8x_EqU1_iuX_lWivjmyirmEdN2a-rYBceUKCWGmKRulDpH4e_H0VLR7-IqQ"
