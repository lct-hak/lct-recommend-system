import pandas as pd
import numpy as np
from scipy import sparse
from sklearn.preprocessing import normalize

TOP_RESULTS = 10


class Recommender:
    def recommend(self, user_id: int, interactions_df: pd.DataFrame, categories_df: pd.DataFrame):
        categories_dict = self._get_categories_dict(categories_df)
        rows, r_pos = self._get_items_and_indexes(interactions_df.values[:, 0])
        cols, c_pos = self._get_items_and_indexes(interactions_df.values[:, 1])
        interactions_sparse = self._get_sparse_matrix(interactions_df.values[:, 2], r_pos, c_pos)
        interactions_sparse_transposed = interactions_sparse.transpose(copy=True)

        # User-Item
        Pui = normalize(interactions_sparse, norm='l2', axis=1)
        # Item-User
        Piu = normalize(interactions_sparse_transposed, norm='l2', axis=1)
        fit = Pui * Piu * Pui

        return [categories_dict[i+1] for i in fit.getrow(user_id).toarray().argsort()[0][-TOP_RESULTS:].tolist()]

    def _get_categories_dict(self, categories_df: pd.DataFrame) -> dict:
        categories_df.index = categories_df['id']
        return categories_df['category'].to_dict()

    def _get_items_and_indexes(self, values):
        return np.unique(values, return_inverse=True)

    def _get_sparse_matrix(self, values, r_pos, c_pos):
        return sparse.csr_matrix((values, (r_pos, c_pos)))
