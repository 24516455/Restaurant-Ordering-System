# features/promotions/__init__.py

from flask import Blueprint

promotions_bp = Blueprint('promotions', __name__)

from . import routes  # 导入路由
