import os

import django
from django.db import IntegrityError

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()
from django.test import TestCase

from tabom.models import Article, User
from tabom.services.like_service import do_like


class TestLikeService(TestCase):
    def test_a_user_can_like_an_article(self) -> None:
        # given
        user = User.objects.create(name="test")
        article = Article.objects.create(title="test_title")

        # when
        like = do_like(user.id, article.id)

        # then
        # id 가 들어있다는 것은 데이터베이스로부터 id를 발급받았다는 뜻
        # 즉, 성공적으로 insert가 되었다는 증거
        self.assertIsNotNone(like.id)
        self.assertEqual(user.id, like.user_id)
        self.assertEqual(article.id, like.article_id)

    def test_a_user_can_like_an_article_only_once(self) -> None:
        # given
        user = User.objects.create(name="test")
        article = Article.objects.create(title="test_title")

        # except
        like1 = do_like(user.id, article.id)
        # assertRaises의 동작: Exception이 발생하면 통과, 아무일도 안 일어나면 AssertionError를 일으킴
        with self.assertRaises(IntegrityError):
            like2 = do_like(user.id, article.id)
