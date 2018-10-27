import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "reference_project.settings")

import django
django.setup()

from jobs.models import Job
from faker import Faker

fake_data_gen = Faker()

def populate(N=5):
    for entry in range(N):
        fake_summary = fake_data_gen.company()
        fake_image = fake_data_gen.file_name(extension="jpeg")

        job_page = Job.objects.get_or_create(summary=fake_summary, image=fake_image)




if __name__ == '__main__':
    print("populating script!")
    populate()
    print("populating complete!")
