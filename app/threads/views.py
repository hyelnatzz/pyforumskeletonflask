from . import threads_bp


@threads_bp.route('/view/<int:post_id>/', methods=['GET'])
def view_post(post_id):
    return f'View Post {post_id}'


@threads_bp.route('/edit/<int:post_id>/', methods=['GET', 'POST'])
def edit_post(post_id):
    return f'Edit Post {post_id}'


@threads_bp.route('/delete/<int:post_id>/', methods=['POST'])
def delete_post(post_id):
    return f'Delete Post {post_id}'


@threads_bp.route('/categories', methods=['GET'])
def view_categories():
    return 'List of Category view'
