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

        self.sec_id_list = []

        # Bond values
        self.cusip = ''
        self.ratings = ''
        self.desc_append = ''
        self.bond_type = ''
        self.coupon_type = ''
        self.callable = False
        self.putable = False
        self.coupon = 0
        self.convertible = False
        self.maturity = ''
        self.issue_date = ''
        self.next_option_date = ''
        self.next_option_type = ''
        self.next_option_partial = False
        self.notes = ''
