from django.contrib.auth import user_logged_in

from tabom.models import Article, Like, User


def do_like(user_id: int, article_id: int) -> Like:
    """
    get을 할 필요가 없는 이유
    - Foreign key contraint이 있기 때문에

    user_id:
        - 이 id의 user가 실제로 있는 경우
        - 실제로 없는 경우

    article_id:
        - 이 id의 article이 실제로 있는 경우
        - 실제로 없는 경우

    4가지의 경우 수가 있지만 사실 like로 받을 수 있는 것은 user_id와 article_id가
    실제로 있을 경우에만 가능하므로 2가지이며,
    둘 중 하나라도 실제로 없는 경우에는 Foreign key constraint에 의해 알아서 걸러짐(insert 되지않음)
    - db가 지켜줌(정합성을)
    - 따라서 지금은 크게 신경 안써도 됨
    """

    return Like.objects.create(user_id=user_id, article_id=article_id)
