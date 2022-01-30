import os
import random
import uuid


def stats_image_upload_to(instance, filename):
    ext = filename.split('.')[-1]

    path = 'stats/image/{}/{}/'.format('{}'.format(random.randint(0, 256)),
                                       '{}'.format(random.randint(0, 256)), )

    filename = '{}_{}.{}'.format(random.randint(1, 99),
                                 uuid.uuid4(),
                                 ext.lower())

    return os.path.join(path, filename)
