import asyncpg



class TestSenderList:
    def __init__(self, connector: asyncpg.pool.Pool):
        self.connector = connector

    async def get_users(self):
        query = f"CREATE TABLE IF NOT EXISTS test3_table (user_id bigint NOT NULL, user_name char," \
                    f"active char NOT NULL, PRIMARY KEY (user_id))"
        await self.connector.execute(query)





#     async with connector.acquire(name_table) as connect:
#         name_table = 'datausers'
#         query = f"SELECT user_id FROM {name_table}"
#         results_query: List[Record] = await connect.fetch(query)
#         return [result.get('user_id') for result in results_query]
#
#
# async def get_user(name_table):
#     users_ids = await get_users(name_table)
#     for user_id in users_ids:
#         print(str(user_id))






