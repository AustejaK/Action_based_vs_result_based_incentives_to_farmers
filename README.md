# Action_based_vs_result_based_incentives_to_farmers
 This is an oTree software for an experiment on farmers' preferences towards result-based and action-based subsidies.
 
This study is a joint work with Claudia Magnapera, Simone Cerroni, Roberta Raffaelli, and Rudy Nayga Jr. This study was conducted as a part of EU Horizon 2020 project "VISIONARY".

In settings.py, please define:

    dict(
        name='visionary_feed_add',
        display_name="VISIONARY: essential oils for methane reduction",
        app_sequence=['visionary_feed_add'],
        num_demo_participants=5,
        TREATMENT='RBS',
        policy_mix='30'
    ),
    
and

    PARTICIPANT_FIELDS = ['TREATMENT'] 


