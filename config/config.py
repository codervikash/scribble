import os
from models import model
from google.appengine.api import app_identity

PRODUCTION = os.environ.get('SERVER_SOFTWARE', '').startswith('Google App Eng')
DEBUG = DEVELOPMENT = not PRODUCTION

APPLICATION_ID = app_identity.get_application_id()
CURRENT_VERSION_ID = os.environ.get('CURRENT_VERSION_ID')
CURRENT_VERSION_NAME = CURRENT_VERSION_ID.split('.')[0]

CONFIG_DB = model.Config.get_master_db()

CSRF_SECRET_KEY = 'csrf_secret_key'

ADMIN = {
    'FIRST_NAME': '',
    'LAST_NAME': '',
    'EMAIL': '',
    'MOBILE': '',
    'TIMEZONE': 'UTC+05:30'
}

APPLICATION_CONFIG = {
  'webapp2_extras.auth': {
    'user_model': 'models.model.User',
    'user_attributes': ['email_address', 'first_name', 'mobile_no', 'is_admin']
  },
  'webapp2_extras.sessions': {
    'secret_key': 'your_scret_key'
  }
}
