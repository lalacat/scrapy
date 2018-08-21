import os
from scrapy.settings import Settings

#s = Settings()
def job_dir(settings):
    #path = settings['JOBDIR']
    path = settings['JOBDIR']
    if path and not os.path.exists(path):
        os.makedirs(path)
    return path


