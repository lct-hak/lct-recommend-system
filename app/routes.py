from app import app, models, db
from recommender import Recommender
import pandas as pd


@app.route('/recommend/<user_id>')
def get_csv(user_id: int):
    recommender = Recommender()

    interactions_statement = "SELECT user_id, group_id, COUNT(*) as interactions_count " \
                             "FROM interaction " \
                             "GROUP BY user_id, group_id " \
                             "HAVING COUNT(*) > 1"
    categories_statement = 'SELECT id, category FROM "group"'

    interactions_df = pd.read_sql(interactions_statement, db.session.connection())
    categories_df = pd.read_sql(categories_statement, db.session.connection())

    return recommender.recommend(user_id, interactions_df, categories_df)
