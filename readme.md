<b>Important</b>: You need to be logged in to access the endpoints. To login, [visit the admin panel](https://mozio-test-a.herokuapp.com/admin). \
<br>
To see the API documentation, visit: https://mozio-test-a.herokuapp.com/swagger \
<br>
<hr>

# API Endpoints
* Add a new service area through admin panel: https://mozio-test-a.herokuapp.com/admin/serviceareas/servicearea/add/
* `GET /providers/`: Get all providers.
* `POST /providers/`: Create a provider.
* `GET /providers/{id}`: Get a provider with the given id.
* `PUT /providers/{id}`: Update a provider with the given id.
* `DELETE /providers/{id}`: Delete a provider.
* `GET /serviceareas/`: Get all service areas.
* `POST /serviceareas/`: Create a service area.
* `GET /serviceareas/{id}`: Get a service area with the given id.
* `PUT /serviceareas/{id}`: Update a service area with the given id.
* `DELETE /serviceareas/{id}`: Delete a service area.
* `GET /serviceareas/intercepting_polygons`: See the polygons intersecting a given point. Example: https://mozio-test-a.herokuapp.com/serviceareas/intercepting_polygons/?point={"lat":8.123213123,"lng":3.8979889}

<hr>

Some very basic tests [here](https://github.com/akaanug/MozioServiceArea/blob/main/serviceareas/tests.py).
