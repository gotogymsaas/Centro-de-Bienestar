from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'www', 'project_gotogym.urls',    name='www'),
    host(r'br',  'project_gotogym.urls_br', name='br'),
    host(r'co',  'project_gotogym.urls_co', name='co'),
    host(r'us',  'project_gotogym.urls_us', name='us'),
)
