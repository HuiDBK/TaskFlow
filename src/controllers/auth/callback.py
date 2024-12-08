#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Hui
# @File: callback.py
# @Desc: { 模块描述 }
# @Date: 2024/12/07 16:08
from fastapi import Query
from fastapi.responses import RedirectResponse
from py_tools.logging import logger

from src.controllers.base import BaseController
from src.services.oauth import GithubOAuthService
from src.settings import auth_setting, frontend_index_url


class AuthCallback(BaseController):
    @classmethod
    async def github_callback(cls, code: str = Query(description="授权码"), state: str = Query(None)):
        logger.info(f"Github callback: {code}, {state}")
        oauth_service = GithubOAuthService(auth_setting.github_client_id, auth_setting.github_client_secret)
        try:
            oauth_token = await oauth_service.handle_callback(code)
            redirect_uri = f"{frontend_index_url}?oauth_token={oauth_token}" ""
            response = RedirectResponse(redirect_uri, headers={"oauth_token": oauth_token})
            response.set_cookie(
                key="oauth_token", value=oauth_token, max_age=auth_setting.auth_expires_delta.total_seconds()
            )
            return response
        except Exception:
            logger.error("Github callback error")
            return RedirectResponse(frontend_index_url)
