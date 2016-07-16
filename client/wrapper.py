class Wrapper(object):
    @staticmethod
    def error(msg):
        return msg

    @staticmethod
    def build_error(error_id, error_code, error_msg):
        return "%d | %d | %s" % (error_id, error_code, error_msg)

    @staticmethod
    def connection_closed():
        return 'Connection Closed'

    def tick_price(self, ticker_id, field, price, can_auto_execute): pass

    def tick_size(self, ticker_id, field, size): pass

    def tick_option_computation(self, ticker_id, field, implied_vol, delta, opt_price,
                                pv_dividend, gamma, vega, theta, und_price): pass

    def tick_generic(self, ticker_id, tick_type, value): pass

    def tick_string(self, ticker_id, tick_type, value): pass

    def tick_efp(self, ticker_id, tick_type, basis_points, formatted_basis_points,
                 implied_future, hold_days, future_expiry, dividend_impact,
                 dividend_to_expiry): pass

    def order_status(self, order_id, status, filled, remaining, avg_fill_price, perm_id,
                     parent_id, last_fill_price, client_id, why_held): pass

    def open_order(self, order_id, contract, order, order_state): pass

    def open_order_end(self): pass

    def update_account_value(self, key, value, currency, account_name): pass

    def update_portfolio(self, contract, position, market_price, market_value, avg_cost,
                         unrealized_pnl, realized_pnl, account_name): pass

    def update_account_time(self, time_stamp): pass

    def account_download_end(self, account_name): pass

    def next_valid_id(self, order_id): pass

    def contract_details(self, req_id, contract_details): pass

    def bond_contract_details(self, req_id, contract_details): pass

    def contract_detail_end(self, req_id): pass

    def exec_details(self, req_id, contract, execution): pass

    def exec_details_end(self, req_id): pass

    def update_mkt_depth(self, ticker_id, position, operation, side, price, size): pass

    def update_mkt_depth_l2(self, ticker_id, position, market_maker, operation,
                            side, price, size): pass

    def update_news_bulletin(self, msg_id, msg_type, message, orig_exchange): pass

    def managed_accounts(self, account_list): pass

    def receive_fa(self, fa_data_type, xml): pass

    def historical_data(self, req_id, date, open, high, low, close, volume,
                        count, wap, has_gaps): pass

    def scanner_parameters(self, xml): pass

    def scanner_data(self, req_id, rank, contract_details, distance, benchmark,
                     projection, legs_str): pass

    def scanner_data_end(self, req_id): pass

    def real_time_bar(self, req_id, time, open, high, low, close, volume, wap, count): pass

    def current_time(self, time): pass

    def fundamental_data(self, req_id, data): pass

    def delta_neutral_validation(self, req_id, under_comp): pass

    def tick_snapshot_end(self, req_id): pass

    def market_data_type(self, req_id, market_data_type): pass

    def commission_report(self, commission_report): pass

    def position(self, account, contract, pos, avg_cost): pass

    def position_end(self): pass

    def account_summary(self, req_id, account, tag, value, currency): pass

    def account_summary_end(self, req_id): pass

    def verify_message_api(self, api_data): pass

    def verify_completed(self, is_successful, error_text): pass

    def display_group_list(self, req_id, groups): pass

    def display_group_updated(self, req_id, contract_info): pass
