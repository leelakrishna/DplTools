from pyramid.session import UnencryptedCookieSessionFactoryConfig
from pyramid.config import Configurator
import matplotlib
matplotlib.use('Agg')

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    my_session_factory = UnencryptedCookieSessionFactoryConfig('picnicsecret')
    config = Configurator(settings=settings, session_factory=my_session_factory)
    config.add_static_view('static', 'static', cache_max_age=3600)
    #data availability
    config.add_route('dataAvailability', '/dataAvailability')
    
    #image gen
    config.add_route('imagereq', '/rti_request/')#will set up process, and forward to progress#
    config.add_route('imageresult', '/rti_result/{session}')#
    config.add_route('imagegen', '/{accesstype}/{access}/custom_rti/')

    #netcdf gen
    config.add_route('netcdfreq', '/netcdf_request/')#
    config.add_route('netcdfgen', '/{accesstype}/{access}/custom_netcdf/')

    #month
    config.add_route('thumb', '/{accesstype}/{access}/{thumbtype}/')#goes to month
    config.add_route('month', '/{accesstype}/{access}/{thumbtype}/{year}/{month}/')
    config.add_route('multiview', '/{accesstype}/{access}/all/{year}/{month}/{day}/')
    #images
    config.add_route('today', '/{accesstype}/{access}/')#goes to today
    config.add_route('date','/{accesstype}/{access}/{year}/{month}/{day}/{ampm}/')
    #portal
    config.add_route('home', '/')

    #utilities
    config.add_route('session_resource','/session/{session}/{filename}')
    config.add_route('image_resource','/{accesstype}/{access}/{year}/{month}/{day}/{filename}')
    config.add_route('resource_request','/statichash/{statickey}')#static file
    config.add_route('progress', '/progress/')#
    config.add_route('progress_withid', '/progress/{session}')#
    config.add_route('select_month','/selectmonth')
    config.add_route('select_day','/selectday')
    config.add_route('status','/status')
    config.add_route('debug','/debug')
    config.add_route('debugsession','/debug/{session}')

    config.scan()
    return config.make_wsgi_app()
