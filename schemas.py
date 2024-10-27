from pydantic import BaseModel
from datetime import date

class Record(BaseModel):
    board_id: str
    trade_date: date
    short_name: str
    sec_id: str
    num_trades: int
    value: float | None = None
    open_val: float | None = None
    low_val: float | None = None
    high_val: float | None = None
    legal_close_price: float | None = None
    wap_price: float | None = None
    close_val: float | None = None
    volume: int | None = None
    market_price_2: float | None = None
    market_price_3: float | None = None
    admittedquote: float | None = None
    mp_2_val_trd: float | None = None
    market_price_3_trades_value: float | None = None
    admittedvalue: float | None = None
    waval: int | None = 0
    trading_session: int | None = None
    curren_cyid: str
    trendclspr: float | None = None
