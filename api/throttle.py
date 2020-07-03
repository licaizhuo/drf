from rest_framework.throttling import SimpleRateThrottle


class SendMessageRate(SimpleRateThrottle):
    scope = "send"

    def get_cache_key(self, request, view):
        phone = request.query_params.get("phone")
        if phone:
            return 'throttle_%(scope)s_%(ident)s' % {"scope": self.scope, "ident": phone}
        return None
