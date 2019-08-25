#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Valuation service implementation"""

from __future__ import print_function
import pandas as pd


class ValuationService:

    def __init__(self, data, matching, currency):
        self.data = data
        self.matching = matching.set_index('matching_id')
        self.currency = currency.set_index('currency')

    def total_price(self, df):
        df['total_price'] = df.apply(
            lambda row: float(row.ratio * row.price * row.quantity), axis = 1
        )
        return df

    def limit_by_top_priced_count(self, df):
        def top_priced_count(dfg):
            matching_id = dfg.matching_id.iloc[0]
            matching = self.matching.loc[matching_id]
            sorted_group = dfg.sort_values(by='total_price', ascending=False)
            return sorted_group.head(matching.top_priced_count)

        return df.groupby(df['matching_id']).apply(top_priced_count)

    def aggregate_prices(self, df):
        aggregate = df[['matching_id', 'price', 'total_price']].groupby(
            df['matching_id']
        ).agg({'price': "mean", 'total_price': "sum"})
        aggregate['price'] = round(aggregate['price'], 1)
        aggregate.rename(columns={'price': 'avg_price'}, inplace=True)
        return aggregate


def main():

    vs = ValuationService(
        data=pd.read_csv("data/data.csv"),
        matching=pd.read_csv("data/matching.csv"),
        currency=pd.read_csv("data/currency.csv")
    )
    res = vs.data.copy()
    res = pd.merge(res, vs.matching, on='matching_id', how='left')
    res = pd.merge(res, vs.currency, on='currency', how='left')

    res = vs.total_price(res)
    res = vs.limit_by_top_priced_count(res)
    res = vs.aggregate_prices(res)

    res.to_csv("data/top_products.csv")


if __name__ == '__main__':
    main()
