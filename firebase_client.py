"""
Firebase Firestore client for state persistence
Handles initialization, connection retries, and error recovery
"""
import json
import logging
from typing import Optional, Dict, Any
from datetime import datetime

import firebase_admin
from firebase_admin import credentials, firestore, exceptions
from