import ckan.plugins as plugins

class DomainObjectModificationExtension(
    plugins.SingletonPlugin, plugins.ISession
): ...
