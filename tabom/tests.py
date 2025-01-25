import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from django.test import TestCase

from tabom.models import User


class TestAutoNow(TestCase):
    """
    django의 TestCase 클래스를 상속하는 클래스를 만든다.
    class 의 이름은 test로 시작해야 함. (pytest에서는 무조건적인 규칙인데,
    unit test 에서는 강제는 아님)
        - unit test -> 파이썬 언어 자체에 내장된 테스트 프레임워크
        - pytest -> 서드 파티 라이브러리 (poetry add 로 추가해야함) 사실 상 파이썬 표준
    """

    def test_auto_now_field_is_set_when_save(self) -> None:
        """
        모든 테스트 함수는 None을 리턴함
        테스트 함수는 3가지 단계로 이루어진다.

        given (주어진)
        테스트의 대상이 되는 재료를 만든다.
            e.g) 좋아요를 하려면 좋아요를 하는 유저와, 대상이 되는 게시글이 필요. 이 둘을 생성함.

        when
            실제로 검증해야 하는 동작을 수행함
                e.g.) 좋아요를 하는 함수를 호출함

        then
            정상적으로 수행이 되는지 검증함
                e.g.) 좋아요 row가 데이터베이스에 insert 되었는지 확인함.
        """

        # given
        user = User(name="test")

        # when
        user.save()  # 실제로 db에 insert 쿼리가 날아가는 시점

        # then
        # 상속에 의해서 assertXXX 메소드들을 물려받음
        self.assertIsNotNone(user.updated_at)  # user.updated_at이 None이 아님을 검증함
        self.assertIsNotNone(user.created_at)

    def test_sample(self) -> None:
        assert 1 + 1 == 2
