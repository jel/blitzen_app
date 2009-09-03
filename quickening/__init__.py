# -*- coding: utf-8 -*-
APP_DEPENDENCIES = {
}

MIDDLEWARE_DEPENDENCIES = {
    'django.middleware.cache.UpdateCacheMiddleware':            None,

    'django.middleware.common.CommonMiddleware':                (
        'django.middleware.cache.UpdateCacheMiddleware',
    ),

    'django.middleware.cache.FetchFromCacheMiddleware':         (
        'django.middleware.common.CommonMiddleware',
    ),
}
