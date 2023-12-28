
import functions_framework
from google.cloud import spanner

instance_id = "test-instance"
database_id = "example-db"

client = spanner.Client()
instance = client.instance(instance_id)
database = instance.database(database_id)

@functions_framework.http
def spanner_read_data(req):
    query = 'select * from Albums'

    outputs = []
    with database.snapshot() as snapshot:
        results = snapshot.execute_sql(query)

        for row in results:
            output = "SingerId: {}, AlbumId: {}, AlbumTitle: {}".format(*row)
            outputs.append(output)

    return "\n".join(outputs)