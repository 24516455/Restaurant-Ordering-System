# features/user_account/__init__.py

from flask import Blueprint

user_account_bp = Blueprint('user_account', __name__)

from . import routes  # 导入路由
