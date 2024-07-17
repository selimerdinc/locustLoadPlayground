from locust import HttpUser, task, between


class UserBehavior(HttpUser):
    wait_time = between(1, 5)
    host = "https://reqres.in"

    @task
    def get_users(self):
        self.client.get("/api/users?page=2")

    @task
    def get_single_user(self):
        self.client.get("/api/users/2")

    @task
    def create_user(self):
        payload = {"name": "morpheus", "job": "leader"}
        self.client.post("/api/users", json=payload)

    @task
    def update_user(self):
        payload = {"name": "morpheus", "job": "zion resident"}
        self.client.put("/api/users/2", json=payload)

    @task
    def delete_user(self):
        self.client.delete("/api/users/2")
