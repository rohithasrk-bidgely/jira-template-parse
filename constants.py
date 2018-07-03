TYPE_OPTIONS = ['Configuration', 'Code Deployment', 'Configuration Change']

SEQUENCE = {
    'Redshift Scripts': 1,
    'CQL Scripts': 2,
    'RDS Scripts': 3,
    'Data Server/Api Server Deployment': 4,
    'Data Server/Api Server Scripts': 5,
}

BUILD_VERSIONS = {
    'Pingpong': '3.1.',
    'HAN NA Disagg': '1.0.',
    'GB Disagg': '1.0.',
    'HAN EU Disagg': '2.0.',
    'Hybrid model version': '3.1.',
}

BACKEND_DEPLOYMENT = {
        'GBDisagg': 1,
        'HANDisagg': 2,
        'SIH Binary': 3,
        'aggregationServices': 4,
        'coretoolservices': 5,
        'datacubejobs': 6,
        'devToolServices': 7,
        'emailservices': 8,
        'gbIntegration': 9,
        'goaleventservices': 10,
        'ingesterclient': 11,
        'ingesterjobs': 12,
        'nhoodservices': 13,
        'notifications': 14,
        'pdfGenerationService': 15,
        'rawDataManager': 16,
        'reportservices': 17,
        'scheduler': 18,
        'sms': 19,
        'uploadSplitterServices': 20,
        'watchdog': 21,
        'geo-adapter': 22,
        'HANDisagg-2': 23,
        'HANDisagg-1': 24,
        'notificationsprocessorservice': 25,
}

FRONTEND_DEPLOYMENT = {
     'Angular': 1,
     'Admin Tool': 2,
     'Mobile (UE, HO)': 3,
     'Mobile (homebeat)': 4,
     'Drupal': 5,
     'Mobile Web  (HO)': 6,
     'SMS Assets': 7,
     'Mobile (Enovos)': 8,
}
