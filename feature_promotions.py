
# features/promotions/__init__.py

from flask import Blueprint

promotions_bp = Blueprint('promotions', __name__)

from . import routes  # 导入路由

# features/promotions/routes.py

from flask import render_template
from . import promotions_bp

@promotions_bp.route('/promotions')
def promotions():
    # 此处可以从数据库查询并显示促销信息
    return render_template('promotions.html')

<!-- features/promotions/templates/promotions.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>促销活动</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <h1>当前促销活动</h1>
    <!-- 显示促销活动细节 -->
    <p>敬请期待！</p>
</body>
</html>

