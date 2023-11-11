from . import update_bounds

_handlers = [update_bounds.handler]
handlers = {handler.type: handler for handler in _handlers}
