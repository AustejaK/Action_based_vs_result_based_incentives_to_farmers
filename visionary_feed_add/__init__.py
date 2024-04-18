from otree.api import *

import itertools
import random


doc = """
Experiment of use of essential oils in methane reduction. October 2023.
Author: Austėja Kažemekaitytė (University of Trento), a.kazemekaityte@unitn.it
Joint work wit

IMPORTANT:
1. Select treatment: 'RBS' (result-based subsidy) or 'CC' (carbon credit)
2. Select policy mix condition: 10, 30, 40 
    10 = 10% action-based subsidy and 90% result-based subsidy
    30 = 30% action-based subsidy and 70% result-based subsidy
    50 = 50% action-based subsidy and 50% result-based subsidy
"""


class C(BaseConstants):
    NAME_IN_URL = 'visionary_feed_add'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    standard_subsidy = [986, 1052, 1118, 1183, 1249, 1315, 1578]
    rbs_cc = [1077, 1156, 1236,	1315, 1394, 1473, 1552]

    distribution_bins = ['6.6%; 7%',
                         '7.1%; 7.5%',
                         '7.6%; 8%',
                         '8.1%; 8.5%',
                         '8.6%; 9%',
                         '9.1%; 9.5%',
                         '9.6%; 10%'
                         ]

    distribution_real = [1, 6, 12, 21, 12, 11, 7] # to be checked
    distribution_methane = [7, 11, 12, 21, 12, 6, 1]

    farm_income = 20000
    essential_oils = 1315

    pm_40_60 = [1014, 1062, 1109, 1157, 1204, 1252, 1300]
    pm_60_40 = [983, 1015, 1046, 1078, 1110, 1141, 1173]
    pm_80_20 = [952, 968, 983, 999, 1015, 1031, 1047]

    activities = [
        dict(name='nessun', label='Nessun\'altra attività'),
        dict(name='mele', label='Coltivazione di mele'),
        dict(name='viticoltura', label='Viticoltura/Vinificazione'),
        dict(name='foraggi', label='Produzione di foraggi'),
        dict(name='latte', label='Solo allevamento di bestiame da latte'),
        dict(name='altro', label='Altro, specificare'),
    ]
class Subsession(BaseSubsession):
    pass

def creating_session(subsession):
    if subsession.round_number == 1:
        for player in subsession.get_players():
            participant = player.participant
            participant.treatment = subsession.session.config['TREATMENT']

            player.policy_mix_1 = subsession.session.config['policy_mix']

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    name = models.StringField()
    birthplace = models.StringField()
    birthday = models.StringField()
    city = models.StringField()
    street = models.StringField()
    number = models.StringField()
    email = models.StringField()

    consent = models.IntegerField(widget=widgets.RadioSelectHorizontal,
        label='Ciò premesso,', choices=[(1, 'DO IL MIO CONSENSO A PARTECIPARE ALLO STUDIO 1')])

    privacy = models.IntegerField(widget=widgets.RadioSelectHorizontal,
                                  label='',
                                  choices=[(1, 'PER PRESA VISIONE DELL’INFORMATIVA PRIVACY')])

    consent2 = models.IntegerField(widget=widgets.RadioSelectHorizontal,
        label='', choices=[(1, 'DO IL MIO CONSENSO A PARTECIPARE ALLO STUDIO 2')])

    treatment = models.StringField()

    mpl1_1 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3])
    mpl1_2 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3])
    mpl1_3 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3])
    mpl1_4 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3])
    mpl1_5 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3])
    mpl1_6 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3])
    mpl1_7 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3])

    mpl_no_switching = models.IntegerField()
    pm_no_switching = models.IntegerField()

    mpl2_ub = models.IntegerField()
    mpl2_lb = models.IntegerField()

    mpl2_1 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3])
    mpl2_2 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3])
    mpl2_3 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3])
    mpl2_4 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3])

    mpl2_1_subsidy = models.IntegerField()
    mpl2_2_subsidy = models.IntegerField()
    mpl2_3_subsidy = models.IntegerField()
    mpl2_4_subsidy = models.IntegerField()

    lowest_stand_subsidy = models.IntegerField()

    policy_mix_1 = models.IntegerField()

    pm1_1 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3])
    pm1_2 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3])
    pm1_3 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3])
    pm1_4 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3])
    pm1_5 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3])
    pm1_6 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3])
    pm1_7 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3])


    pm2_1 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3])
    pm2_2 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3])
    pm2_3 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3])
    pm2_4 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3])
    pm2_5 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3])
    pm2_6 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3])

    slider1 = models.IntegerField(min=0, max=70, blank=True)
    slider2 = models.IntegerField(min=0, max=70, blank=True)
    slider3 = models.IntegerField(min=0, max=70, blank=True)
    slider4 = models.IntegerField(min=0, max=70, blank=True)
    slider5 = models.IntegerField(min=0, max=70, blank=True)
    slider6 = models.IntegerField(min=0, max=70, blank=True)
    slider7 = models.IntegerField(min=0, max=70, blank=True)

    frequency_payoff = models.IntegerField()

    comprehension_1 = models.IntegerField(widget=widgets.RadioSelect,
                                          choices=[(1, "1,315 €"),
                                                   (2, "1,077 €"),
                                                   (3, "L'importo dipende da quale dei sette intervalli viene estratto "
                                                       "in modo casuale."),
                                                   (4, "Non so/non ricordo")],
                                          label="La mia risposta è:")

    opinion_essential_oil = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=[[0, "0 (molto improbabile)"],
                                                                                       [1, "1"], [2, "2"], [3, "3"],
                                                                                       [4, "4"], [5, "5"], [6, "6"],
                                                                                       [7,
                                                                                        "7 (molto probabile)"]],
                                        label="")

    opinion_ss = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=[[0, "0 (molto improbabile)"],
                                                                                       [1, "1"], [2, "2"], [3, "3"],
                                                                                       [4, "4"], [5, "5"], [6, "6"],
                                                                                       [7,
                                                                                        "7 (molto probabile)"]],
                                        label="")

    opinion_rbs_cc = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=[[0, "0 (molto improbabile)"],
                                                                                       [1, "1"], [2, "2"], [3, "3"],
                                                                                       [4, "4"], [5, "5"], [6, "6"],
                                                                                       [7,
                                                                                        "7 (molto probabile)"]],
                                        label="")

    opinion_ss_vs_rbs_cc = models.IntegerField(widget=widgets.RadioSelect, choices=[0, 1],
                                        label="")

    study1phase = models.IntegerField()
    mpl_task = models.IntegerField()
    reduction = models.IntegerField()
    reddito = models.IntegerField()
    option = models.IntegerField()

    payoff_phase_1 = models.CurrencyField()
    payoff_phase_2 = models.CurrencyField()

    # Questionnaire
    sesso = models.BooleanField(widget=widgets.RadioSelect, choices=[(0, 'M'), (1, 'F')], label='1. Sesso:')
    anno = models.IntegerField(label='2. Il suo anno di nascita:')
    istruzione = models.IntegerField(widget=widgets.RadioSelect, choices=[(0, 'Scuola elementare'),
                                                                          (1, 'Diploma di scuola media'),
                                                                          (2, 'Diploma di scuola superiore o equivalente'),
                                                                          (3, 'Laurea triennale'),
                                                                          (4, 'Laurea magistrale (o a ciclo unico)'),
                                                                          (5, 'Diploma di specializzazione')],
                                     label='3. Qual è il livello più alto di istruzione che ha conseguito?')

    proprietario = models.BooleanField(widget=widgets.RadioSelect, choices=[(0, 'Sì'), (1, 'No')], label='1. E’ il/la proprietario/a dell’azienda agricola?')
    valle = models.IntegerField(widget=widgets.RadioSelect, choices=[(0, 'Valle di Sole'),
                                                                     (1, 'Valle di Non'),
                                                                     (2, 'Valle dei Laghi'),
                                                                     (3, 'Paganella'),
                                                                     (4, 'Rotaliana-Konigsberg'),
                                                                     (5, 'Valle di Cembra'),
                                                                     (6, 'Altipiani cimbri'),
                                                                     (7, 'Alto Garda e Ledro'),
                                                                     (8, 'Valli Giudicarie'),
                                                                     (9, 'Val d’Adige'),
                                                                     (10, 'Alta Valsugana e Bersntol'),
                                                                     (11, 'Valsugana e Tesino'),
                                                                     (12, 'Primiero'),
                                                                     (13, 'Comun General De Fascia'),
                                                                     (14, 'Val Di Fiemme'),
                                                                     (15, 'Vallagarina'),
                                                                     (16, 'Altro')],
                                label='2. In quale valle della provincia di Trento è localizzato la sua azienda agricola?')

    generazione = models.BooleanField(widget=widgets.RadioSelect, choices=[(0, 'Sì'), (1, 'No')], label='3. E’ un allevatore/allevatrice di prima generazione?')
    esperienza = models.FloatField(label='4. Quanti anni di esperienza ha in allevamenti di bovine da latte? [inserisci gli anni]')
    vacche_bruna = models.IntegerField(blank=True)
    vacche_frisona = models.IntegerField(blank=True)
    vacche_pezzata = models.IntegerField(blank=True)
    vacche_rendena = models.IntegerField(blank=True)
    vacche_grigiaalpina = models.IntegerField(blank=True)
    vacche_altro = models.StringField(blank=True)

    # attivita = models.StringField(widget=widgets.RadioSelect,
    #     choices=['Nessun\'altra attività', 'Coltivazione di mele', 'Viticoltura/Vinificazione', 'Produzione di foraggi ', 'Altro'],
    #              label='5. Oltre all\'allevamento di bestiame da latte, quale altra attività agricola svolge?')

    nessun = models.BooleanField(blank=True)
    mele = models.BooleanField(blank=True)
    viticoltura = models.BooleanField(blank=True)
    foraggi = models.BooleanField(blank=True)
    altro = models.BooleanField(blank=True)

    attivita_other = models.StringField(
        label="Specificare:", blank=True)

    foragi = models.StringField(label='6. Percentuale di foraggi autoprodotti (nel 2022): [inserire la percentuale]')

    ostacoli = models.StringField(widget=widgets.RadioSelect, choices=['Fortemente in disaccordo', 'In disaccordo ',
                                                                       'Né in disaccordo né d’accordo ', 'D’accordo',
                                                                       'Fortemente d’accordo'],
                                  label='2. Non vedo grandi ostacoli nel somministrare degli olii essenziali nel mio allevamento. Quanto è d’accordo con questa affermazione:')

    alimentazione = models.StringField(widget=widgets.RadioSelect,
                                       choices=['Pre-miscelato', 'Unifeed', 'Altro'],
                                       label='7. Tipo di pratica esecutiva utilizzata per l\'alimentazione dei propri animali')
    alimentazione_other = models.StringField(label="Specificare:", blank=True)


    razione = models.FloatField(label='8. Qual è il costo medio di una razione completa per vacca da latte (al giorno)? '
                                       '[inserire il numero]')

    vacche = models.StringField(label='10. Quante vacche in lattazione ha nella sua azienda? [inserire il numero]')

    latte = models.StringField(label='11. Quanti litri/quintali di latte produce in media all\'anno? Si prega di '
                                     'specificare in lettere se ha inserito litri o quintali. '
                                      '[inserire il numero]')
    prodotto = models.StringField(widget=widgets.RadioSelect, choices=['Concast Trentingrana ',
                                                                       'LatteTrento ', 'Gruppo Poli ',
                                                                       'Altro'],
                                  label="15. Dove conferisce il latte prodotto?")
    zona = models.IntegerField(widget=widgets.RadioSelect, choices=[(0, 'Sì'), (1, 'No'), (2, 'Non lo so')],
                               label='16. La vostra azienda si trova in una delle Zone Vulnerabili '
                                     'da Nitrati (ZVN) di origine agricola?')
    allevamento = models.IntegerField(widget=widgets.RadioSelect, choices=[(0, 'Con lettiera con paglia o altro '
                                                                               'materiale assorbente (letame)'),
                                                                           (1, 'Con pavimento grigliato (liquame)'),
                                                                           (2, 'Ho un allevamento all’aperto')],
                               label='17. Come avviene la raccolta delle deiezioni nel suo allevamento?')
    biogas = models.FloatField(label='15. Quale percentuale di letame/liquame conferisce agli impianti di biogas?')
    stoccaggio = models.IntegerField(widget=widgets.RadioSelect, choices=[(0, 'Vasche chiuse'),
                                                                           (1, 'Vasche aperte'),
                                                                           (2, 'Altro')],
                               label='18. Quale sistema di stoccaggio delle deiezioni c’è nel suo allevamento?')

    pannelli = models.IntegerField(widget=widgets.RadioSelect, choices=[(0, 'Sì'), (1, 'No')],
                               label='20. Avete pannelli fotovoltaici/solari sulle vostre stalle/strutture agricole?')
    iniziativa = models.StringField(label='21. Oltre quelle già nominate (installazione di pannelli fotovoltaici, '
                                          'conferimento letame agli impianti biogas) c\'è qualche altra iniziativa che '
                                          'ha attuato nella sua azienda per ridurre l\'impatto ambientale? '
                                          '[Specificare]')
    ricavo = models.StringField(label='1. Qual è stato il suo ricavo medio lordo per vacca nel 2022?')
    costi = models.StringField(label='2. Quali sono stati i suoi costi medi per vacca nel 2022?')

    latte_percentuale = models.StringField(label='Latte alimentare: inserire la percentuale')
    formaggi_percentuale = models.StringField(label='Produzione di formaggi: inserire la percentuale')
    auto_produzione = models.FloatField(label='11. Del latte prodotto, quale percentuale è destinata '
                                               'all\'auto-produzione di formaggi? ')

    reduction_necessary = models.StringField(widget=widgets.RadioSelect,
        choices=['Fortemente in disaccordo', 'In disaccordo',
                                                      'Né in disaccordo né d’accordo ', 'D’accordo',
                                                      'Fortemente d’accordo'],
                                             label='1. E’ necessario ridurre il metano della fermentazione enterica. Quanto è d’accordo '
                                                   'con questa affermazione:')

    nep1 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5])
    nep2 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5])
    nep3 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5])
    nep4 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5])
    nep5 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5])
    nep6 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5])
    nep7 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5])

    risk1 = models.IntegerField(widget=widgets.RadioSelect, choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    risk2 = models.IntegerField(widget=widgets.RadioSelect, choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    risk3 = models.IntegerField(widget=widgets.RadioSelect, choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    risk4 = models.IntegerField(widget=widgets.RadioSelect, choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    pbc1 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5])
    pbc2 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5])
    pbc3 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5])
    pbc4 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5])
    pbc5 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5])
    pbc6 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5])

    ambiguity1 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5])
    ambiguity2 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5])
    ambiguity3 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5])
    ambiguity4 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5])
    ambiguity5 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5])
    ambiguity6 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5])

    minimum_subsidy = models.IntegerField(widget=widgets.RadioSelect, choices=[(1, "Sì, accetterei un importo minore "
                                                                                   "di 937€ (75%)"),
                                                                               (2, "No, l’importo minimo che accetterei "
                                                                                   "è 937€ (75%)")],
                                          label="")
    minimum_subsidy_1 = models.StringField(label="", blank=True)
    minimum_subsidy_1_higher = models.CurrencyField(label="", blank=True)

    minimum_subsidy_2 = models.IntegerField(widget=widgets.RadioSelect, choices=[(1, "Sì, accetterei un importo minore "
                                                                                   "di 937€ (75%)"),
                                                                               (2, "No, l’importo minimo che accetterei "
                                                                                   "è 937€ (75%)")],
                                          label="")
    minimum_subsidy_3 = models.StringField(label="", blank=True)
    minimum_subsidy_3_higher = models.CurrencyField(label="", blank=True)



# PAGES
class Start(Page):
    pass

class Consent(Page):
    form_model = 'player'
    form_fields = ['name', 'birthplace', 'birthday', 'city', 'street', 'number', 'email', 'consent', 'consent2']


class Privacy(Page):
    form_model = 'player'
    form_fields = ['privacy']

class Waiting_page(Page): # for participants waiting for others to arrive at the page
    pass

class Introduction_1(Page):
    pass

class Introduction_1a(Page):
    pass

class Introduction_1b(Page):
    pass

class Introduction_2(Page):
    pass

class Introduction_3(Page):
    pass

class Introduction_4(Page):
    pass

class Introduction_phase_1(Page):
    pass

class Introduction_study_1(Page):
    pass

class Introduction_5(Page):
    pass

class Introduction_6(Page):
    pass

class Introduction_7(Page):
    pass


# MPL instructions

class Phase_1_a(Page):
    pass

class Phase_1_a_2(Page):
    pass

class Phase_1_a_3(Page):
    pass

class Phase_1_a_4(Page):
    pass

class Phase_1_a_5(Page):
    pass

class Phase_1_a_6(Page):
    pass

class Phase_1_a_7(Page):
    pass

class Phase_1_a_8(Page):
    pass


class Phase_1_b(Page):
    pass

# class Phase_1_b_2(Page):
#     form_model = 'player'
#     form_fields = ['opinion_essential_oil']

class Phase_1_c(Page):
    pass

class Phase_1_d(Page):
    pass

class Phase_1_e(Page):
    pass

class Phase_1_e_2(Page):
    pass

# class Phase_1_e_3(Page):
#     form_model = 'player'
#     form_fields = ['opinion_ss']

class Phase_1_f(Page):
    pass

class Phase_1_f_2(Page):
    pass

class Phase_1_f_3(Page):
    pass

# class Phase_1_f_4(Page):
#     form_model = 'player'
#     form_fields = ['opinion_rbs_cc']
#
# class Phase_1_f_5(Page):
#     form_model = 'player'
#     form_fields =  ['opinion_ss_vs_rbs_cc']

class Phase_1_g(Page):
    pass

class Phase_1_h(Page):
    pass

class Phase_1_h_2(Page):
    pass

class Phase_1_h_3(Page):
    pass

class Phase_1_h_4(Page):
    pass

class Phase_1_i(Page):
    pass

class Phase_1_i_2(Page):
    pass

class Phase_1_j(Page):
    pass

class Phase_1_k(Page):
    pass

class Phase_1_k_2(Page):
    pass

class Phase_1_k_2_ex1(Page):
    pass

class Phase_1_k_2_ex2(Page):
    pass

class Phase_1_k_2_ex3(Page):
    pass

class Phase_1_k_3(Page):
    pass

class Phase_1_k_4(Page):
    pass

class Phase_1_k_5(Page):
    pass

class Phase_1_k_6(Page):
    pass

class Phase_1_k_7(Page):
    pass

class Phase_1_k_8(Page):
    pass

class Phase_1_l(Page):
    pass

class Phase_1_m(Page):
    pass

class Phase_1_n(Page):
    pass

class Phase_1_o_ex1(Page):
    pass

class Phase_1_o_ex1b(Page):
    pass

class Phase_1_o_ex2_1(Page):
    pass

class Phase_1_o_ex2_2(Page):
    pass

class Phase_1_o_ex2_3(Page):
    pass

class Phase_1_o_ex2_4(Page):
    pass

class Phase_1_o_ex2_4_2(Page):
    pass

class Phase_1_o_ex2_5(Page):
    pass

class Phase_1_o_ex3(Page):
    pass

class Phase_1_o_ex3_2(Page):
    pass

class Phase_1_p(Page):
    pass

class Phase_1_p_2(Page):
    pass

class Phase_1_r(Page):
    pass

class Comprehension_questions_1(Page):
    form_model = 'player'
    form_fields = ['comprehension_1']

class Comprehension_questions_1b(Page):
    pass


# Phase 1: Multiple price list
class Phase_1_task(Page):
    pass


class Phase_1_task_1(Page):
    form_model = 'player'
    form_fields = ['mpl1_1']

class Phase_1_task_2(Page):
    form_model = 'player'
    form_fields = ['mpl1_2']

class Phase_1_task_3(Page):
    form_model = 'player'
    form_fields = ['mpl1_3']

class Phase_1_task_4(Page):
    form_model = 'player'
    form_fields = ['mpl1_4']

class Phase_1_task_5(Page):
    form_model = 'player'
    form_fields = ['mpl1_5']

class Phase_1_task_6(Page):
    form_model = 'player'
    form_fields = ['mpl1_6']

class Phase_1_task_7(Page):
    form_model = 'player'
    form_fields = ['mpl1_7']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        choice_vector = [player.mpl1_1, player.mpl1_2, player.mpl1_3, player.mpl1_4, player.mpl1_5, player.mpl1_6, player.mpl1_7]
        # Check if participants had NO switching behaviour
        same_choices = choice_vector.count(choice_vector[0]) == len(choice_vector)
        if same_choices is True:
            player.mpl_no_switching = choice_vector[0]
        else:
            player.mpl_no_switching = 0

        # # Check when participants switched to standard subsidy
        # if player.mpl_no_switching == 0:
        #     index_of_1 = None
        #     for index in range(len(choice_vector)):
        #         if choice_vector[index] == 1:
        #             index_of_1 = index
        #             break
        #     # Define bounds for second stage
        #     if index_of_1 is not None:
        #         player.mpl2_ub = C.standard_subsidy[index_of_1]
        #         if index_of_1 > 0:
        #             player.mpl2_lb = C.standard_subsidy[index_of_1-1]
        #         else:
        #             player.mpl2_lb = C.standard_subsidy[index_of_1]
        #             player.mpl2_ub = C.standard_subsidy[index_of_1+1]
        #
        #     difference = player.mpl2_ub - player.mpl2_lb
        #
        #     player.mpl2_1_subsidy = player.mpl2_lb + round(difference/5)
        #     player.mpl2_2_subsidy = player.mpl2_lb + round(difference / 5)*2
        #     player.mpl2_3_subsidy = player.mpl2_lb + round(difference / 5)*3
        #     player.mpl2_4_subsidy = player.mpl2_lb + round(difference / 5)*4

class Phase_1_additional_question(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.mpl_no_switching > 0

    form_model = 'player'
    form_fields = ['minimum_subsidy', 'minimum_subsidy_1']

# Policy mix
class Phase_2(Page):
    pass

class Phase_2_a(Page):
    pass


class Phase_2_b(Page):
    @staticmethod
    def vars_for_template(player: Player):
        pm = 100 - player.policy_mix_1
        return dict(pm=pm)


class Phase_2_b_1(Page):
    pass


class Phase_2_b_2(Page):
    pass


class Phase_2_c(Page):
    @staticmethod
    def vars_for_template(player: Player):
        pm = 100 - player.policy_mix_1
        return dict(pm=pm)



class Phase_2_c_2(Page):
    @staticmethod
    def vars_for_template(player: Player):
        pm = 100 - player.policy_mix_1
        return dict(pm=pm)

class Phase_2_c_3(Page):
    pass


class Phase_2_c_4(Page):
    @staticmethod
    def vars_for_template(player: Player):
        pm = 100 - player.policy_mix_1
        return dict(pm=pm)

class Phase_2_c_5(Page):
    @staticmethod
    def vars_for_template(player: Player):
        pm = 100 - player.policy_mix_1
        return dict(pm=pm)


class Phase_2_c_6(Page):
    @staticmethod
    def vars_for_template(player: Player):
        pm = 100 - player.policy_mix_1
        return dict(pm=pm)


class Phase_2_c_7(Page):
    @staticmethod
    def vars_for_template(player: Player):
        pm = 100 - player.policy_mix_1
        return dict(pm=pm)

class Phase_2_c_7_2(Page):
    pass


class Phase_2_c_8(Page):
    pass


class Phase_2_c_8_2(Page):
    pass


class Phase_2_c_9(Page):
    pass


class Phase_2_c_10(Page):
    pass


class Phase_2_d(Page):
    pass


class Phase_2_d_2(Page):
    pass


class Phase_2_e(Page):
    pass


class Phase_2_f(Page):
    pass


class Phase_2_g(Page):
    pass


class Phase_2_part_1(Page):
    pass

class Phase_2_task_1(Page):
    form_model = 'player'
    form_fields = ['pm1_1']

    @staticmethod
    def vars_for_template(player: Player):
        pm = 100 - player.policy_mix_1
        return dict(pm=pm)


class Phase_2_task_2(Page):
    form_model = 'player'
    form_fields = ['pm1_2']

    @staticmethod
    def vars_for_template(player: Player):
        pm = 100 - player.policy_mix_1
        return dict(pm=pm)


class Phase_2_task_3(Page):
    form_model = 'player'
    form_fields = ['pm1_3']

    @staticmethod
    def vars_for_template(player: Player):
        pm = 100 - player.policy_mix_1
        return dict(pm=pm)


class Phase_2_task_4(Page):
    form_model = 'player'
    form_fields = ['pm1_4']

    @staticmethod
    def vars_for_template(player: Player):
        pm = 100 - player.policy_mix_1
        return dict(pm=pm)


class Phase_2_task_5(Page):
    form_model = 'player'
    form_fields = ['pm1_5']

    @staticmethod
    def vars_for_template(player: Player):
        pm = 100 - player.policy_mix_1
        return dict(pm=pm)


class Phase_2_task_6(Page):
    form_model = 'player'
    form_fields = ['pm1_6']

    @staticmethod
    def vars_for_template(player: Player):
        pm = 100 - player.policy_mix_1
        return dict(pm=pm)


class Phase_2_task_7(Page):
    form_model = 'player'
    form_fields = ['pm1_7']

    @staticmethod
    def vars_for_template(player: Player):
        pm = 100 - player.policy_mix_1
        return dict(pm=pm)

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        choice_vector = [player.pm1_1, player.pm1_2, player.pm1_3, player.pm1_4, player.pm1_5, player.pm1_6, player.pm1_7]
        # Check if participants had NO switching behaviour
        same_choices = choice_vector.count(choice_vector[0]) == len(choice_vector)
        if same_choices is True:
            player.pm_no_switching = choice_vector[0]
        else:
            player.pm_no_switching = 0

class Phase_2_additional_question(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.pm_no_switching > 0

    form_model = 'player'
    form_fields = ['minimum_subsidy_2', 'minimum_subsidy_3']

# Beliefs about methane reduction
class Phase_3(Page):
    pass


class Phase_3_instructions_1(Page):
    pass


class Phase_3_instructions_2(Page):
    pass


class Phase_3_instructions_3(Page):
    pass


class Phase_3_instructions_4(Page):
    pass

class Phase_3_instructions_4_2(Page):
    pass

class Phase_3_instructions_5(Page):
    pass

class Phase_3_instructions_5_2(Page):
    pass


class Phase_3_instructions_6(Page):
    pass

class Phase_3_instructions_6_2(Page):
    pass

class Phase_3_start(Page):
    pass


class Phase_3_task(Page):
    form_model = 'player'
    form_fields = ['slider1', 'slider2', 'slider3', 'slider4',
                   'slider5', 'slider6', 'slider7']

    @staticmethod
    def error_message(player: Player, values):
        if values['slider1'] + values['slider2'] + values['slider3'] + values['slider4'] \
                + values['slider5'] + values['slider6'] + values['slider7'] != 70:
            return "La somma dei gettoni utilizzati deve essere uguale a 70."

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        answers_task_1 = []
        answers_task_1.extend([player.slider1, player.slider2, player.slider3, player.slider4, player.slider5,
                               player.slider6, player.slider7])
        margins_list_lower_bound = []
        margins_list_higher_bound = []

        for item in answers_task_1:
            if item == 70:
                margin = 7
            elif 69 >= item >= 60:
                margin = 6
            elif 59 <= item <= 50:
                margin = 5
            elif 49 <= item <= 40:
                margin = 4
            elif 30 <= item <= 39:
                margin = 3
            elif 20 <= item <= 29:
                margin = 2
            else:
                margin = 1

            margins_list_higher_bound.append(item + margin)
            margins_list_lower_bound.append(item - margin)
            print(margins_list_lower_bound)
            print(margins_list_higher_bound)

        correct_answers = []
        for index, item in enumerate(answers_task_1):
            if margins_list_lower_bound[index] <= C.distribution_methane[index] <= margins_list_higher_bound[index]:
                correct_answers.append(C.distribution_methane[index])
            else:
                correct_answers.append(-1)

        player.frequency_payoff = 1 if correct_answers == C.distribution_methane else 0

# Ending questionnaire
class Questionnaire_introduction(Page):
    pass


class Questionnaire_1(Page):
    form_model = 'player'
    form_fields = ['sesso', 'anno', 'istruzione']


class Questionnaire_2(Page):
    form_model = 'player'
    form_fields = ['proprietario', 'valle', 'generazione', 'esperienza']


class Questionnaire_3(Page):
    form_model = 'player'
    form_fields = ['vacche', 'vacche_bruna',
                   'vacche_frisona', 'vacche_pezzata',
                   'vacche_rendena', 'vacche_grigiaalpina',
                   'vacche_altro']


class Questionnaire_4(Page):
    form_model = 'player'
    # form_fields = ['attivita', 'attivita_other', 'foragi']

    @staticmethod
    def get_form_fields(player: Player):
        questions = [lang['name'] for lang in C.activities]
        questions_others = questions + ["attivita_other", "foragi"]
        return questions_others

    @staticmethod
    def error_message(player: Player, values):
        # print('values is', values)
        num_selected = 0
        for lang in C.activities:
            if values[lang['name']]:
                num_selected += 1
        if num_selected < 1:
            return "You must select at least 1 option."


class Questionnaire_5(Page):
    form_model = 'player'
    form_fields = ['alimentazione', 'alimentazione_other', 'razione']


class Questionnaire_6(Page):
    form_model = 'player'
    form_fields = ['vacche', 'latte', 'auto_produzione']


class Questionnaire_7(Page):
    form_model = 'player'
    form_fields = ['zona', 'biogas', 'pannelli']


class Questionnaire_8(Page):
    form_model = 'player'
    form_fields = ['reduction_necessary', 'ostacoli']


class Questionnaire_8_2(Page):
    form_model = 'player'
    form_fields = ['nep1', 'nep2', 'nep3', 'nep4', 'nep5', 'nep6', 'nep7']


class Questionnaire_9(Page):
    form_model = 'player'
    form_fields = ['risk1', 'risk2', 'risk3', 'risk4']

class Questionnaire_10(Page):
    form_model = 'player'
    form_fields = ['ambiguity1', 'ambiguity2', 'ambiguity3', 'ambiguity4', 'ambiguity5', 'ambiguity6']

class Questionnaire_11(Page):
    form_model = 'player'
    form_fields = ['ricavo', 'costi']

# Ending pages
class Ending_1(Page):
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        # Study 1 phase
        random_phase = random.randint(1, 2)
        player.study1phase = random_phase
        # Random choice within the phase
        random_choice_mpl = random.randint(1, 7)
        player.mpl_task = random_choice_mpl
        # Methane reduction
        numbers = [1, 2, 3, 4, 5, 6, 7]
        # Draw a random number based on the specified probabilities
        random_number = random.choices(numbers, weights=C.distribution_methane, k=1)[0]
        player.reduction = random_number
        # Methane reduction payoff in policy mix
        if player.policy_mix_1 == 40:
            pm_payment = C.pm_40_60[player.reduction-1]
        else:
            if player.policy_mix_1 == 60:
                pm_payment = C.pm_60_40[player.reduction-1]
            else:
                pm_payment = C.pm_80_20[player.reduction-1]

        # Payoff function
        if player.mpl_task == 1:
            if player.study1phase == 1:
                if player.mpl1_1 == 1:
                    player.option = 1
                    player.reddito = C.farm_income - C.essential_oils + C.standard_subsidy[0]
                else:
                    if player.mpl1_1 == 2:
                        player.option = 2
                        player.reddito = C.farm_income - C.essential_oils + C.rbs_cc[player.reduction-1]
                    else:
                        player.option = 3
                        player.reddito = C.farm_income
            else:
                if player.pm1_1 == 1:
                    player.option = 1
                    player.reddito = C.farm_income - C.essential_oils + C.standard_subsidy[0]
                else:
                    if player.pm1_1 == 2:
                        player.option = 2
                        player.reddito = C.farm_income - C.essential_oils + pm_payment
                    else:
                        player.option = 3
                        player.reddito = C.farm_income
        else:
            if player.mpl_task == 2:
                if player.study1phase == 1:
                    if player.mpl1_2 == 1:
                        player.option = 1
                        player.reddito = C.farm_income - C.essential_oils + C.standard_subsidy[1]
                    else:
                        if player.mpl1_2 == 2:
                            player.option = 2
                            player.reddito = C.farm_income - C.essential_oils + C.rbs_cc[player.reduction - 1]
                        else:
                            player.option = 3
                            player.reddito = C.farm_income
                else:
                    if player.pm1_2 == 1:
                        player.option = 1
                        player.reddito = C.farm_income - C.essential_oils + C.standard_subsidy[1]
                    else:
                        if player.pm1_2 == 2:
                            player.option = 2
                            player.reddito = C.farm_income - C.essential_oils + pm_payment
                        else:
                            player.option = 3
                            player.reddito = C.farm_income
            else:
                if player.mpl_task == 3:
                    if player.study1phase == 1:
                        if player.mpl1_3 == 1:
                            player.option = 1
                            player.reddito = C.farm_income - C.essential_oils + C.standard_subsidy[2]
                        else:
                            if player.mpl1_3 == 2:
                                player.option = 2
                                player.reddito = C.farm_income - C.essential_oils + C.rbs_cc[player.reduction - 1]
                            else:
                                player.option = 3
                                player.reddito = C.farm_income
                    else:
                        if player.pm1_3 == 1:
                            player.option = 1
                            player.reddito = C.farm_income - C.essential_oils + C.standard_subsidy[2]
                        else:
                            if player.pm1_3 == 2:
                                player.option = 2
                                player.reddito = C.farm_income - C.essential_oils + pm_payment
                            else:
                                player.option = 3
                                player.reddito = C.farm_income
                else:
                    if player.mpl_task == 4:
                        if player.study1phase == 1:
                            if player.mpl1_4 == 1:
                                player.option = 1
                                player.reddito = C.farm_income - C.essential_oils + C.standard_subsidy[3]
                            else:
                                if player.mpl1_4 == 2:
                                    player.option = 2
                                    player.reddito = C.farm_income - C.essential_oils + C.rbs_cc[player.reduction - 1]
                                else:
                                    player.option = 3
                                    player.redito = C.farm_income
                        else:
                            if player.pm1_4 == 1:
                                player.option = 1
                                player.reddito = C.farm_income - C.essential_oils + C.standard_subsidy[3]
                            else:
                                if player.pm1_4 == 2:
                                    player.option = 2
                                    player.reddito = C.farm_income - C.essential_oils + pm_payment
                                else:
                                    player.option = 3
                                    player.reddito = C.farm_income
                    else:
                        if player.mpl_task == 5:
                            if player.study1phase == 1:
                                if player.mpl1_5 == 1:
                                    player.option = 1
                                    player.reddito = C.farm_income - C.essential_oils + C.standard_subsidy[4]
                                else:
                                    if player.mpl1_5 == 2:
                                        player.option = 2
                                        player.reddito = C.farm_income - C.essential_oils + C.rbs_cc[player.reduction - 1]
                                    else:
                                        player.option = 3
                                        player.reddito = C.farm_income
                            else:
                                if player.pm1_5 == 1:
                                    player.option = 1
                                    player.reddito = C.farm_income - C.essential_oils + C.standard_subsidy[4]
                                else:
                                    if player.pm1_5 == 2:
                                        player.option = 2
                                        player.reddito = C.farm_income - C.essential_oils + pm_payment
                                    else:
                                        player.option = 3
                                        player.reddito = C.farm_income
                        else:
                            if player.mpl_task == 6:
                                if player.study1phase == 1:
                                    if player.mpl1_6 == 1:
                                        player.option = 1
                                        player.reddito = C.farm_income - C.essential_oils + C.standard_subsidy[5]
                                    else:
                                        if player.mpl1_6 == 2:
                                            player.option = 2
                                            player.reddito = C.farm_income - C.essential_oils + C.rbs_cc[
                                                player.reduction - 1]
                                        else:
                                            player.option = 3
                                            player.reddito = C.farm_income
                                else:
                                    if player.pm1_6 == 1:
                                        player.option = 1
                                        player.reddito = C.farm_income - C.essential_oils + C.standard_subsidy[5]
                                    else:
                                        if player.pm1_6 == 2:
                                            player.option = 2
                                            player.reddito = C.farm_income - C.essential_oils + pm_payment
                                        else:
                                            player.option = 3
                                            player.reddito = C.farm_income
                            else:
                                if player.study1phase == 1:
                                    if player.mpl1_7 == 1:
                                        player.option = 1
                                        player.reddito = C.farm_income - C.essential_oils + C.standard_subsidy[6]
                                    else:
                                        if player.mpl1_7 == 2:
                                            player.option = 2
                                            player.reddito = C.farm_income - C.essential_oils + C.rbs_cc[
                                                player.reduction - 1]
                                        else:
                                            player.option = 3
                                            player.reddito = C.farm_income
                                else:
                                    if player.pm1_7 == 1:
                                        player.option = 1
                                        player.reddito = C.farm_income - C.essential_oils + C.standard_subsidy[6]
                                    else:
                                        if player.pm1_7 == 2:
                                            player.option = 2
                                            player.reddito = C.farm_income - C.essential_oils + pm_payment
                                        else:
                                            player.option = 3
                                            player.reddito = C.farm_income

        player.payoff_phase_1 = 15 * ((player.reddito-19605)/(20863-19605))
        if player.frequency_payoff == 1:
            player.payoff_phase_2 = 15
        else:
            player.payoff_phase_2 = 0


class Ending_2(Page):
    pass

class Ending_3(Page):
    @staticmethod
    def vars_for_template(player: Player):
        percentage_list = [75, 80, 85, 90, 95, 100, 120]
        methane_list = [179.52,	192.72,	205.92,	219.12,	232.32,	245.52,	258.72]
        methane = methane_list[player.reduction-1]
        percentages = percentage_list[player.mpl_task-1]
        if player.study1phase == 1:
            methane_payment = C.rbs_cc[player.reduction-1]
        else:
            if player.policy_mix_1 == 40:
                methane_payment = C.pm_40_60[player.reduction - 1]
            else:
                if player.policy_mix_1 == 60:
                    methane_payment = C.pm_60_40[player.reduction - 1]
                else:
                    methane_payment = C.pm_80_20[player.reduction - 1]
        policy_mix_2 = 100 - player.policy_mix_1
        return dict(percentages=percentages, methane=methane, methane_payment=methane_payment, policy_mix_2=policy_mix_2)


class Ending_4(Page):
    pass

class Ending_5(Page):
    @staticmethod
    def vars_for_template(player: Player):
        payoff_tot = 10*2 + player.payoff_phase_1 + player.payoff_phase_2
        return dict(payoff=payoff_tot)


page_sequence = [
    Start,
    Consent,
    Privacy,
    Introduction_1,
    Introduction_1a,
    Introduction_1b,
    Introduction_2,
    Introduction_3,
    Introduction_4,
    Introduction_study_1,
    Introduction_5,
    Introduction_phase_1,
    # Phase_1_a,
    # Phase_1_a_2,
    # Phase_1_a_3,
    # Phase_1_a_4,
    # Phase_1_a_5,
    # Phase_1_a_6,
    # Phase_1_a_7,
    Phase_1_a_8,
    Phase_1_b,
    Phase_1_c,
    Phase_1_d,
    Phase_1_e,
    Phase_1_e_2,
    Phase_1_f,
    Phase_1_f_2,
    Phase_1_f_3,
    Phase_1_g,
    Phase_1_h,
    Phase_1_h_2,
    Phase_1_h_3,
    Phase_1_h_4,
    Phase_1_i,
    Phase_1_i_2,
    Phase_1_k,
    Phase_1_k_2,
    Phase_1_k_2_ex1,
    Phase_1_k_2_ex2,
    Phase_1_k_2_ex3,
    Phase_1_o_ex2_2,
    Phase_1_o_ex2_3,
    Phase_1_o_ex2_4,
    Phase_1_o_ex2_4_2,
    # Phase_1_k_3,
    # Phase_1_k_5,
    # Phase_1_k_7,
    Phase_1_k_6,
    Phase_1_k_8,
    Phase_1_l,
    Introduction_6,
    Phase_1_n,
    Phase_1_p,
    Phase_1_p_2,
    Phase_1_r,
    Phase_1_task,
    Phase_1_task_1,
    Phase_1_task_2,
    Phase_1_task_3,
    Phase_1_task_4,
    Phase_1_task_5,
    Phase_1_task_6,
    Phase_1_task_7,
    Phase_1_additional_question,
    Phase_2,
    Phase_2_a,
    Phase_2_b,
    Phase_2_c,
    Phase_2_c_2,
    Phase_2_b_1,
    Phase_2_b_2,
    Phase_2_c_3,
    Phase_2_c_6,
    Phase_2_c_7,
    Phase_2_c_7_2,
    Phase_2_c_8,
    Phase_2_c_8_2,
    Phase_2_c_9,
    Phase_2_c_10,
    Phase_2_g,
    Phase_2_part_1,
    Phase_2_task_1,
    Phase_2_task_2,
    Phase_2_task_3,
    Phase_2_task_4,
    Phase_2_task_5,
    Phase_2_task_6,
    Phase_2_task_7,
    Phase_2_additional_question,
    Phase_3,
    Phase_3_instructions_1,
    Phase_3_instructions_3,
    Phase_3_instructions_4,
    Phase_3_instructions_4_2,
    Phase_3_instructions_5,
    Phase_3_instructions_5_2,
    Phase_3_instructions_6,
    Phase_3_instructions_6_2,
    Phase_3_instructions_2,
    Phase_3_start,
    Phase_3_task,
    Questionnaire_introduction,
    Questionnaire_1,
    Questionnaire_2,
    Questionnaire_4,
    Questionnaire_5,
    Questionnaire_6,
    Questionnaire_7,
    Questionnaire_8,
    Questionnaire_8_2,
    Questionnaire_9,
    Questionnaire_10,
    Questionnaire_11,
    Ending_1,
    Ending_2,
    Ending_3,
    Ending_4,
    Ending_5
]
