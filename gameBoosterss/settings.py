from dotenv import load_dotenv
import os
from pathlib import Path
import firebase_admin
from firebase_admin import credentials
load_dotenv()


BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.getenv('SECRET_KEY')
print("SECRET_KEY",SECRET_KEY)
DEBUG = os.getenv('DEBUG') == 'True'
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

AUTH_USER_MODEL = 'accounts.BaseUser'


ASGI_APPLICATION = 'gameBoosterss.asgi.application'

# redis 
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    }
}
# CHANNEL_LAYERS = {
#     "default": {
#         "BACKEND": "channels_redis.core.RedisChannelLayer",
#         "CONFIG": {
#             "hosts": [("localhost", 6379)],
#         },
#     },
# }

# Application definition
INSTALLED_APPS = [
    # web_socket and server
    'daphne',
    'channels',
    'simple_history',

    # admin
    'jazzmin',

    # django package
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    # Others
    # 'paypal.standard.ipn',
    'corsheaders',
    'rest_framework',
    'social_django', 

    # serve static file inside server
    'whitenoise.runserver_nostatic',
    
    # My Apps
    'booster.apps.BoosterConfig',
    'customer.apps.CustomerConfig',
    'dashboard.apps.DashboardConfig',
    'wildRift.apps.WildriftConfig',
    'valorant.apps.ValorantConfig',
    'pubg.apps.PubgConfig',
    'tft.apps.TftConfig',
    'hearthstone.apps.HearthstoneConfig',
    'WorldOfWarcraft.apps.WorldofwarcraftConfig',
    'leagueOfLegends.apps.LeagueoflegendsConfig',
    'rocketLeague.apps.RocketleagueConfig',
    'django_cleanup.apps.CleanupConfig',
    'accounts.apps.AccountsConfig',
    'mobileLegends.apps.MobilelegendsConfig',
    'honorOfKings.apps.HonorofkingsConfig',
    'dota2.apps.Dota2Config',
    'overwatch2.apps.Overwatch2Config',
    'csgo2.apps.Csgo2Config',
    'chat.apps.ChatConfig',
    'games.apps.GamesConfig',
    'news.apps.NewsConfig',

    # 'django_q',
    # 'modeltranslation',
    # 'oauth2_provider',
    # 'allauth',
    # 'allauth.account',
    # 'allauth.socialaccount',
    # 'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.facebook',
    # 'django.contrib.sites',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'gameBoosterss.middleware.ImageSizeLimitMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
    # 'dashboard.middleware.AdminLogMiddleware',
        'simple_history.middleware.HistoryRequestMiddleware',

]
CORS_ORIGIN_WHITELIST = [
    'https://www.madboost.gg',
    # 'http://www.madboost.gg',
    # 'http://madboost.gg',
    'https://madboost.gg',
]

# CORS_ALLOW_CREDENTIALS = True 

ROOT_URLCONF = 'gameBoosterss.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/"templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
            ],
        },
    },
]

WSGI_APPLICATION = 'gameBoosterss.wsgi.application'

print("os.getenv('DB_USER'),",os.getenv('DB_USER'),)
print("os.getenv('NAME'),",os.getenv('NAME'),)
print(50 *"7")
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv('NAME'),
        "USER": os.getenv('DB_USER'),
        "PASSWORD": os.getenv('PASSWORD'),
        "HOST": os.getenv('HOST'),
        "PORT": "5432",
    }
}



# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Directory where static files will be collected during deployment
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# STORAGES = {
#     'default': {
#         'BACKEND': "whitenoise.storage.CompressedManifestStaticFilesStorage",
#         # 'OPTIONS': {
#         #     'location': '/path/to/your/static/files',
#         # },
#     },
# }

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# MEDIA_URL = "media/"
MEDIA_URL = "https://storage.googleapis.com/mad-boost.appspot.com/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


# # to send email via gmail
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587  # For TLS
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'madboost.customer@gmail.com'  # Your Gmail address
# EMAIL_HOST_PASSWORD = 'wpmj llfn toax sfil'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.office365.com'  # Outlook SMTP server hostname
EMAIL_PORT = 587  # Port for TLS
EMAIL_USE_TLS = True
EMAIL_HOST_USER =os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')



ALLOWED_HOSTS = [
    '8881-197-32-66-233.ngrok-free.app'
    'https://www.madboost.gg',
    'https://madboost.gg',
    'localhost',
    '127.0.0.1',
    'www.madboost.gg',
    'madboost.gg',
    'gameboost-test-f25426e2eac4.herokuapp.com',
    'www.gameboost-test-f25426e2eac4.herokuapp.com',
    '*' # remove in deplay mode
    ]


# PAYPAL_EMAIL='sb-blcbf28542348@business.example.com'
# # PAYPAL_EMAIL='madboost.payment@gmail.com'
# PAYPAL_TEST = True
# PAYPAL_VERIFY_URL = 'https://www.sandbox.paypal.com/cgi-bin/webscr'
# SECURE_SSL_REDIRECT = True

# settings.py
PAYPAL_CLIENT_ID = 'AWriOlHzu6y-ZS_v4m4NA_vHDXHnEIxrCsickcLYqWKHfaU9l3N7he2mdBOsoosSOUZdYE5P8OEZ8h5c'
PAYPAL_CLIENT_SECRET = 'EFyP_TDyg9yCzyitIltAVhRcfnx6BK3BlfqP7kMO0wljFpi-ppzUdgzh3J_9peN9ib5td2La1ZsZDBJ4'
PAYPAL_MODE = 'sandbox'

# PAYPAL_CLIENT_ID = os.getenv('PAYPAL_CLIENT_ID')
# PAYPAL_CLIENT_SECRET = os.getenv('PAYPAL_CLIENT_SECRET')
# PAYPAL_MODE = 'live'

import paypalrestsdk
# Configure PayPal SDK
paypalrestsdk.configure({
    "mode": PAYPAL_MODE,  # sandbox or live
    "client_id": PAYPAL_CLIENT_ID,
    "client_secret": PAYPAL_CLIENT_SECRET,
})


Q_CLUSTER = {
    'name': 'gameBoosterss',
    'workers': 10,
    'recycle': 500,
    'timeout': 1960,
    'retry': 2000,
    'queue_limit': 50,
    'bulk': 10,
    'orm': 'default',
    'sync': False,
    'cleanup': 500, 
}

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'console': {
#             'class': 'logging.StreamHandler',
#         },
#     },
#     'root': {
#         'handlers': ['console'],
#         'level': 'DEBUG',  # Set to 'DEBUG' for more detailed logs
#     },
#     'loggers': {
#         'django_q': {
#             'handlers': ['console'],
#             'level': 'DEBUG',  # Set to 'DEBUG' for more detailed logs
#             'propagate': True,
#         },
#     },
# }


AUTHENTICATION_BACKENDS = [
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
    # 'allauth.account.auth_backends.AuthenticationBackend',
    'accounts.backends.EmailOrUsernameModelBackend',
]

LOGIN_REDIRECT_URL = '/'

# SOCIALACCOUNT_PROVIDERS = {
#     'google': {
#         'SCOPE': ['profile', 'email'],
#         'AUTH_PARAMS': {'access_type': 'online'},
#         'APP': {
#             'client_id': '563095491808-r4dh48ijatksm45ndj2fphphesi2ppik.apps.googleusercontent.com',
#             'secret': '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',
#         }
#     },
#     'facebook': {
#         'APP': {
#             'client_id': '395531559777062',
#             'secret': 'c20a1e8d9e7ecc668111c23da1528dee',
#         }
#     }
    
    #  'facebook': {
    #     'METHOD': 'oauth2',
    #     'SCOPE': ['email', 'public_profile', 'user_friends'],
    #     'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
    #     'INIT_PARAMS': {'cookie': True},
    #     'FIELDS': [
    #         'id',
    #         'email',
    #         'name',
    #         'first_name',
    #         'last_name',
    #         'verified',
    #         'locale',
    #         'timezone',
    #         'link',
    #         'gender',
    #         'updated_time',
    #     ],
    #     'EXCHANGE_TOKEN': True,
    #     'LOCALE_FUNC': lambda request: 'en_US',
    #     'VERIFIED_EMAIL': False,
    #     'VERSION': 'v12.0',
    #     'APP': {
    #         'client_id': '395531559777062',
    #         'secret': 'c20a1e8d9e7ecc668111c23da1528dee',
    #     }
    # }
# }

# Initialize Firebase Admin SDK
cred = credentials.Certificate(os.path.join(BASE_DIR, 'fire-base.json'))
FIREBASE_STORAGE_BUCKET = "mad-boost.appspot.com"
firebase_admin.initialize_app(cred, {'storageBucket': FIREBASE_STORAGE_BUCKET})

SOCIAL_AUTH_FACEBOOK_KEY = "1103754014333574"
SOCIAL_AUTH_FACEBOOK_SECRET = "73973ab1ae8c0410c167500a0d897e4b"
SOCIAL_AUTH_LOGIN_ERROR_URL = 'https://www.madboost.gg/social-auth-exception/'
SOCIAL_AUTH_FACEBOOK_DEAUTHORIZATION_CALLBACK_URL = "https://www.madboost.gg/facebook-data-deletion/"
SOCIAL_AUTH_FACEBOOK_SCOPE = [
    'email',
]

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '563095491808-r4dh48ijatksm45ndj2fphphesi2ppik.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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',
SOCIAL_AUTH_GOOGLE_OAUTH2_REDIRECT_URI = 'https://www.madboost.gg/social/complete/google-oauth2/'
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'email',
]

# env file 
PAYMENT_KEY = os.getenv('PAYMENT_KEY')
MERCHANT_UUID = os.getenv('MERCHANT_UUID')


# settings.py
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.UserRateThrottle',
        'rest_framework.throttling.AnonRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'user': '100/day',
        'anon': '20/hour',
    }
}


JAZZMIN_SETTINGS = {
    "site_title": "MadBoost Admin",
    "site_header": "MadBoost Admin",
    "login_logo": "favicon.ico",
    "show_sidebar": True,
    "site_icon": "favicon.ico",
    "site_logo": "favicon.ico",
    "welcome_sign": "Welcome to the MadBoost Admin",

    # "navigation_expanded": True,
    "hide_apps": ['auth'],
    "hide_models": ['accounts.TokenForPay', 'accounts.Tip_data'],
    "icons": {
        "auth": "fas fa-users-cog",
        "accounts.Wallet": "fa-solid fa-wallet",
        "accounts.BaseUser": "fa-solid fa-users",
        "accounts.Transaction": "fas fa-money-bill-wave",
        "accounts.BaseOrder": "fas fa-shopping-cart",
    },
    
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-chevron-right",
    "related_modal_active": True,
    "use_google_fonts_cdn": True,
    "changeform_format": "vertical_tabs",
    
    # "show_ui_builder": True,
}

X_FRAME_OPTIONS = 'SAMEORIGIN'