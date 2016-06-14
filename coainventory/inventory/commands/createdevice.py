import os, sys, random
from optparse import make_option

from model_mommy import mommy

from scripts.generators.generator import *

from apps.defendants.models import Defendant
from apps.accounts.models import Agency, Statutes, Division

from ...models import Case, WorthlessCheckCase, CaseType, RequiredDateType

class Command(BaseCommand):
    help = 'Creates Cases(s) for the Agency'
    option_list = BaseCommand.option_list + (
        make_option('--count',
                    default=200,
                    type='int',
                    action='store',
                    dest='cases',
                    help='Number of Cases to create [Default = 200]'),
    )

    def handle(self, *args, **options):
        with transaction.atomic():
            cases = []
            for i in range(0, options['cases']):
                CASE_INFO = {
                    'case_number': create_case_number(),
                    'case_start_date': create_random_date(),
                    'defendant': random.choice(Defendant.objects.all()),
                    'merchants': random.choice(Merchant.objects.all()),
                    'merchant_fee':100,
                    'da_fee':100,
                    'state_fee':100,
                    'check_amount':random.randint(300, 500),
                    'division':random.choice(Division.objects.all()),
                    'case_type':random.choice(CaseType.objects.all())
                }
                case = mommy.make(WorthlessCheckCase, **CASE_INFO)
                for i in range(0,random.randint(1,5)):
                    case.statutes.add(random.choice(Statutes.objects.all()))
                case.save()
                cases.append(case)
            self.stdout.write('Agency has %d Cases' % ( len(cases) ))