# features/promotions/routes.py

from flask import render_template
from . import promotions_bp

@promotions_bp.route('/promotions')
def promotions():
    # 此处可以从数据库查询并显示促销信息
    return render_template('promotions.html')
