from locust import HttpUser, task, between


class ApiUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def test_v1_breeds(self):
        self.client.get("/api/v1/breeds/")

    @task
    def test_v2_breeds(self):
        self.client.get("/api/v2/breeds/")
