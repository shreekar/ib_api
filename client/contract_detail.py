class ContractDetails(object):
    def __init__(self, summary, market_name, min_tick, order_types,
                 valid_exchanges, under_con_id, long_name, contract_month,
                 industry, category, subcategory, time_zone_id, trading_hours,
                 liquid_hours, ev_rule, ev_multiplier):
        self.summary = summary
        self.market_name = market_name
        self.min_tick = min_tick
        self.order_types = order_types
        self.valid_exchange = valid_exchanges
        self.under_con_id = under_con_id
        self.long_name = long_name
        self.contract_month = contract_month
        self.industry = industry
        self.category = category
        self.subcategory = subcategory
        self.time_zone_id = time_zone_id
        self.trading_hours = trading_hours
        self.liquid_hours = liquid_hours
        self.ev_rule = ev_rule
        self.ev_multiplier = ev_multiplier
