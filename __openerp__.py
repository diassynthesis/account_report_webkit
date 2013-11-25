{
    'name': 'Account Report Webkit',
    'description': """
""",
    'version': '1.0',
    'author': 'XCG',
    'license': 'AGPL-3',
    'category': 'Finance',
    'website': '',
    'depends': [
        'account_streamline',
        'report_webkit'
    ],
    'init_xml': [],
    'demo_xml' : [],
    'update_xml': [
        'account_view.xml',
        'data/financial_webkit_header.xml',
        'report/report.xml',
        'wizard/balance_common_view.xml',
        'wizard/general_ledger_wizard_view.xml',
        'wizard/partners_ledger_wizard_view.xml',
        'wizard/trial_balance_wizard_view.xml',
        'wizard/partner_balance_wizard_view.xml',
        'wizard/open_invoices_wizard_view.xml',
        'wizard/print_journal_view.xml',
        'report_menus.xml',
    ],
    'active': False,
    'installable': True,
    'application': True,
}
