from rest_framework_simplejwt.tokens import BlacklistMixin, Token
from backend.core.enums.action_enum import ActionEnum
from typing import Type
from backend.core.exceptions.jwt_exceptions import JWTException
from rest_framework.generics import get_object_or_404
from backend.apps.users.models import UserModel

TokenClass = Type[BlacklistMixin | Token]


class ActivateToken(BlacklistMixin, Token):
    lifetime = ActionEnum.ACTIVATE.exp_time
    token_type = ActionEnum.ACTIVATE.token_type


class RecoveryToken(BlacklistMixin, Token):
    lifetime = ActionEnum.RECOVERY.exp_time
    token_type = ActionEnum.RECOVERY.token_type


class JWTService:
    @staticmethod
    def create_token(user, token_class: TokenClass):
        return token_class.for_user(user)

    @staticmethod
    def token_validate(token, token_class: TokenClass):
        try:
            token_res = token_class(token)
            token_res.check_blacklist()
        except (Exception,):
            raise JWTException
        token_res.blacklist()
        user_id = token_res.payload.get('user_id')
        return get_object_or_404(UserModel, pk=user_id)

