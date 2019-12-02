from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class p1_consent(Page):

    form_model = "player"
    form_fields = ["nombre", "id_number"]

class p2_intro(Page):
    pass

class p3_seller_intro(Page):
    pass

class p4_seller_decision(Page):

    form_model = "player"
    form_fields = ["id_number"]

class p5_seller_list(Page):

    form_model = "player"
    form_fields = ["id_number"]

class p6_buyer_intro(Page):
    pass

class p7_buyer_decision(Page):
    pass

class p8_buyer_sanction(Page):
    pass


page_sequence = [p1_consent, p2_intro, p3_seller_intro, p4_seller_decision, p5_seller_list,
                 p6_buyer_intro, p7_buyer_decision, p8_buyer_sanction]
