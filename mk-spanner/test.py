
# https://cloud.google.com/spanner/docs/getting-started/python
#gcloud spanner instances create test-instance --config=regional-us-central1 --description="Test Instance" --nodes=1

from google.cloud import spanner
from google.cloud.spanner_admin_instance_v1.types import spanner_instance_admin
from google.cloud.spanner_v1 import param_types
from google.type import expr_pb2
from google.iam.v1 import policy_pb2
from google.cloud.spanner_v1.data_types import JsonObject
from google.protobuf import field_mask_pb2  # type: ignore

OPERATION_TIMEOUT_SECONDS = 240

instance_id = 'spanner-dev'
database_id = 'example-db'

client = spanner.Client()
instance = client.instance(instance_id)
database = instance.database(
        database_id,
        ddl_statements=[
            """CREATE TABLE Singers (
            SingerId     INT64 NOT NULL,
            FirstName    STRING(1024),
            LastName     STRING(1024),
            SingerInfo   BYTES(MAX),
            FullName   STRING(2048) AS (
                ARRAY_TO_STRING([FirstName, LastName], " ")
            ) STORED
        ) PRIMARY KEY (SingerId)""",
            """CREATE TABLE Albums (
            SingerId     INT64 NOT NULL,
            AlbumId      INT64 NOT NULL,
            AlbumTitle   STRING(MAX)
        ) PRIMARY KEY (SingerId, AlbumId),
        INTERLEAVE IN PARENT Singers ON DELETE CASCADE""",
        ],
    )

#operation = database.create()
#print("Waiting for operation to complete...")
#operation.result(OPERATION_TIMEOUT_SECONDS)
#print("Created database {} on instance {}".format(database_id, instance_id))

# transactions are called via named functions
# and will pass the transaction in via callbck
def do_inserts(tx):

    row_ct = tx.execute_update(
        "insert into Singers (SingerId, FirstName, LastName) values "
        "(12, 'Melissa', 'Garcia'), "
        "(13, 'Russell', 'Morales'), "
        "(14, 'Jacqueline', 'Long'), "
        "(15, 'Dylan', 'Shaw')"
    )

    print("{} record(s) inserted".format(row_ct))

# Id (how did it know that?) can only exist one time.. one time
#database.run_in_transaction(do_inserts)

def insert_albums(tx):

    #   "(12, 1, 'the first title'), "
    #   "(13, 2, 'the second title')"

    row_ct = tx.execute_update(
        "insert into Albums (SingerId, AlbumId, AlbumTitle) values "
        "(14, 3, 'the third title'), "
        "(15, 4, 'the fourth title')"
    )

    print("{} record(s) inserted".format(row_ct))

#database.run_in_transaction(insert_albums)

with database.snapshot() as snapshot:
    results = snapshot.execute_sql('select SingerId, FirstName, LastName from Singers')

    for row in results:
        print(row)
#
#with database.snapshot() as snapshot:
#    res = snapshot.execute_sql(
#        "select SingerId, FirstName, LastName from Singers "
#        "where LastName = @lastName",
#        params={"lastName": "Garcia"},
#        param_types={"lastName": spanner.param_types.STRING},
#    )
#
#    for row in res:
#        print(row)
#
#with database.snapshot() as snapshot:
#    res = snapshot.execute_sql("select * from Albums")
#    for row in res:
#        print(row)