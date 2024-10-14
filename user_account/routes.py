# features/user_account/routes.py

from flask import render_template
from . import user_account_bp

@user_account_bp.route('/account')
def user_account():
    # 用户账户相关逻辑
    return render_template('user_account.html')
